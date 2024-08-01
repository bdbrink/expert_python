#!/usr/bin/env python3
import boto3
import re
import sys
import logging
from botocore.config import Config

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s", stream=sys.stdout)
logger = logging.getLogger(__name__)

# Configure boto3 client
config = Config(retries={"max_attempts": 10, "mode": "adaptive"})
route53_client = boto3.client("route53", config=config)

# Command line arguments
target_hangar = sys.argv[1]
target_region = sys.argv[2]
domain_base = sys.argv[3]  # e.g., "aws.swacorp.com"
service_name = sys.argv[4]  # e.g., "gateway"

# Global variables
env = None
region_short_code = None
zone_id = None

def get_active_record(record_name):
    response = route53_client.list_resource_record_sets(
        HostedZoneId=zone_id,
        StartRecordName=record_name,
        MaxItems='1'
    )
    records = response["ResourceRecordSets"]
    for record in records:
        if record['Name'] == record_name:
            return record
    return None

def update_record(record_name, target_value, weight=None):
    changes = {
        "Action": "UPSERT",
        "ResourceRecordSet": {
            "Name": record_name,
            "Type": "CNAME",
            "TTL": 60,
            "ResourceRecords": [{"Value": target_value}],
        }
    }
    if weight is not None:
        changes["ResourceRecordSet"]["Weight"] = weight
        changes["ResourceRecordSet"]["SetIdentifier"] = f"{target_hangar} {region_short_code} NLB"

    response = route53_client.change_resource_record_sets(
        HostedZoneId=zone_id,
        ChangeBatch={"Changes": [changes]}
    )
    logger.info(f"Updated record {record_name} to point to {target_value}")
    logger.debug(f"Change info: {response['ChangeInfo']['SubmittedAt']}")

def cutover_service():
    if env == "dev":
        record_name = f"{service_name}.cso.{env}.{domain_base}"
        active_record = get_active_record(record_name)
        if active_record:
            active_value = active_record["ResourceRecords"][0]["Value"]
            logger.info(f"Active record is currently: {active_value}")
            if region_short_code in active_value and target_hangar in active_value:
                logger.error(f"{region_short_code} and {target_hangar} is already the active region: {active_value}")
            else:
                target_value = f"{service_name}.{region_short_code}.observability.{target_hangar}.{env}.{domain_base}"
                update_record(record_name, target_value)
    elif env in ["qa", "prod"]:
        record_name = f"{service_name}-us-weighted.cso.{env}.{domain_base}"
        response = route53_client.list_resource_record_sets(HostedZoneId=zone_id, StartRecordName=record_name)
        records = response["ResourceRecordSets"]
        active_record = next((r for r in records if r.get("Weight") == 255), None)
        if active_record:
            active_value = active_record["ResourceRecords"][0]["Value"]
            logger.info(f"Active record is currently: {active_value}")
            if region_short_code in active_value and target_hangar in active_value:
                logger.error(f"{region_short_code} and {target_hangar} is already the active region: {active_value}")
            else:
                update_record(record_name, active_value, weight=0)  # Set old active to 0
                target_value = f"{service_name}.{region_short_code}.observability.{target_hangar}.{env}.{domain_base}"
                update_record(record_name, target_value, weight=255)  # Set new active to 255
        else:
            logger.error("No active record found with weight 255")

def set_global_variables():
    global env, region_short_code, zone_id

    pattern_env = r"^(dev|qa|prod)\d+$"
    match = re.match(pattern_env, target_hangar)
    if not match:
        logger.error(f"Invalid hangar format: {target_hangar}")
        sys.exit(1)

    env = match.group(1)
    logger.info(f"Environment: {env}")

    # You'll need to maintain a mapping of zone IDs or fetch them dynamically
    zone_ids = {
        "test1": "test_zone"
    }
    zone_id = zone_ids.get(env)
    if not zone_id:
        logger.error(f"No zone ID found for environment: {env}")
        sys.exit(1)

    if target_region not in ["us-east-1", "us-west-2"]:
        logger.error(f"Invalid region: {target_region}. Please specify us-east-1 or us-west-2")
        sys.exit(1)
    region_short_code = "awsuse1" if target_region == "us-east-1" else "awsusw2"

    valid_hangars = ["dev1", "dev2", "qa1", "qa2", "prod2", "prod3"]
    if target_hangar not in valid_hangars:
        logger.error(f"Invalid hangar: {target_hangar}. Must be one of {', '.join(valid_hangars)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: script.py <target_hangar> <target_region> <domain_base> <service_name>")
        sys.exit(1)

    set_global_variables()
    cutover_service()