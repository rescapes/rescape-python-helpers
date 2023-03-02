from .divide import divide
from rescape_python_helpers.pyramda.private.asserts import assert_equal


def test_divide_nocurry():
    assert_equal(divide(10, 5), 2)


def test_divide_curry():
    assert_equal(divide(10)(5), 2)
