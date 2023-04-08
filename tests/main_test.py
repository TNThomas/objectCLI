import pytest

from exceptions import CommandNotSupportedError
from main import execute


class TestExecute:
    def test_unsupported_command(self):
        with pytest.raises(CommandNotSupportedError):
            execute("EXIT", {})
    def test_parse_set(self):
        obj = {}
        assert execute("SET foo=bar", obj) == None