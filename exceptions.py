class ObjectCLIError(Exception):
    pass

class CommandNotSupportedError(ObjectCLIError):
    def __init__(self, command: str, *args: object):
        super().__init__(*args)
        self.command = command

    def __str__(self):
        return f'Command "{self.command}" not supported.'
    
class InvalidPropertyNameError(ObjectCLIError):
    def __init__(self, name: str, *args: object) -> None:
        super().__init__(*args)
        self.name = name

    def __str__(self) -> str:
        return f"Cannot name a property {self.name}."