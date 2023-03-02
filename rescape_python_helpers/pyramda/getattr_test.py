from rescape_python_helpers.pyramda.getattr import getattr
from rescape_python_helpers.pyramda.private.asserts import assert_equal


class TestObject:
    def __init__(self, val):
        self.val = val


test_object = TestObject("foo")


def test_getattr_nocurry():
    assert_equal(getattr("val", test_object), "foo")


def test_getattr_curry():
    assert_equal(getattr("val")(test_object), "foo")
