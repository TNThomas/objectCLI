import pytest

from exceptions import InvalidPropertyNameError
from commands.set import set as SET


class TestSet:
    def test_cannot_set_star(self):
        obj = {}
        with pytest.raises(InvalidPropertyNameError):
            SET(obj, "*=stripe")

    def test_set_str(self):
        obj = {}
        SET(obj, "foo=bar")
        SET(obj, "I=the walrus")
        assert obj == {
            "foo": "bar",
            "I": "the walrus"
        }

    def test_set_int(self):
        obj = {}
        SET(obj, "foo=196")
        SET(obj, "bar=-40")
        SET(obj, "bat=0")
        assert obj == {
            "foo": 196,
            "bar": -40,
            "bat": 0
        }

    def test_set_float(self):
        obj = {}
        SET(obj, "foo=19e-4")
        SET(obj, "bar=-40.7")
        SET(obj, "bat=0.125")
        assert obj == {
            "foo": 19e-4,
            "bar": -40.7,
            "bat": 0.125
        }

    def test_set_bool(self):
        obj = {}
        SET(obj, "foo=True")
        SET(obj, "bar=False")
        assert obj == {
            "foo": True,
            "bar": False
        }

    def test_overwrite_prop(self):
        obj = {"prop": "foo"}
        SET(obj, "prop=bar")
        assert obj == {"prop": "bar"}