from typing import Any

def get_ci(d: dict, key: str) -> Any:
    for k,v in d.items():
        if key.lower() == k.lower():
            return v