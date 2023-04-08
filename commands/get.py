from typing import Any


def get(object: dict[str, Any], arg_str: str) -> Any:
    if arg_str == "*":
        all_entries = ""
        for key in object:
            if all_entries != "":
                all_entries += "\n"
            all_entries += f"{key}={object[key]}"
        return all_entries
    else:
        return object[arg_str]