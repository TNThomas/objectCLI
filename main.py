from typing import Any, Optional

from commands import command_library as commands
from exceptions import CommandNotSupportedError


def execute(command: str, target: dict[str, Any]) -> Optional[str]:
    keyword, args = (command.split(" ", 1) + [""])[:2]
    if keyword == "":
        return
    try:
        fn = commands[keyword]
        return fn(target, args)
    except (KeyError, TypeError):
        raise CommandNotSupportedError(keyword)

def main():
    # The object whose properties to expose
    obj: dict[str, Any] = {}
    # The user input
    cmd: str = ""
    # The message to output, if any
    output_message: Optional[str | Exception] = None
    while cmd != "EXIT":  
        try:
            output_message = execute(cmd, obj)
        except Exception as error:
            output_message = error
        finally:
            # Print non-empty output
            if output_message is not None:
                print(output_message)
        # Get a line of user input
        cmd = input()        

if __name__ == "__main__":
    main()
