from datetime import datetime
from zoneinfo import ZoneInfo

dt = datetime(2024, 7, 25, tzinfo=ZoneInfo("Europe/Warsaw"))
print(dt)