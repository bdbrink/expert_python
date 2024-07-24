from typing import Any

# telling function d needs to be dictionary and key needs to be string
def get_ci(d: dict, key: str) -> Any:
    for k,v in d.items():
        if key.lower() == k.lower():
            return v
