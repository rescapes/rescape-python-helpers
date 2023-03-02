from .subtract import subtract
from rescape_python_helpers.pyramda.private.asserts import assert_equal


def test_subtract_nocurry():
    assert_equal(subtract(4, 3), 1)


def test_subtract_curry():
    assert_equal(subtract(4)(3), 1)
