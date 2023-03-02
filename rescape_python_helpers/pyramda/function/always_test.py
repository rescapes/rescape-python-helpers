from .always import always
from rescape_python_helpers.pyramda.private.asserts import assert_equal


def test_always_nocurry():
    assert_equal(always(3, "foo"), 3)


def test_always_curry():
    always3 = always(3)
    assert_equal(always3("foo"), 3)
