from typing import Any

from exceptions import InvalidPropertyNameError


def set(object: dict[str, Any], arg_str: str) -> None:
    key, value = (arg_str.split("=", 1) + [""])[:2]
    if key == "*":
        raise InvalidPropertyNameError("*")
    stored_value = None
    try:
        stored_value = float(value)
        if stored_value.is_integer():
            stored_value = int(value)
    except ValueError:
        if value in ("True", "False"):
            stored_value = value == "True"
        else:
            stored_value = value
    finally:
        object.update({key: stored_value})
    return