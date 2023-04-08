import pytest
from commands.get import get as GET


class TestGet:
    def test_get_existing_value(self):
        obj = {
            "foo": 42,
            "bar": True,
            "bat": 3.14,
            "baz": "Hello, World!"
        }
        assert GET(obj, "foo") == 42
        assert GET(obj, "bar") == True
        assert GET(obj, "bat") == 3.14
        assert GET(obj, "baz") == "Hello, World!"

    def test_get_nonexistent_value(self):
        obj = {}
        with pytest.raises(KeyError):
            GET(obj, "foo")

    def test_get_all_values(self):
        obj = {
            "foo": 42,
            "bar": True,
            "bat": 3.14,
            "baz": "Hello, World!"
        }
        assert GET(obj, "*") == "foo=42\nbar=True\nbat=3.14\nbaz=Hello, World!"