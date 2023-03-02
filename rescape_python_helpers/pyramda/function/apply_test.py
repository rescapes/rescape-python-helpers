from .apply import apply
from rescape_python_helpers.pyramda.private.asserts import assert_equal


def add(x, y):
    return x + y


def test_apply_nocurry():
    assert_equal(apply(add, [1, 2]), 3)


def test_apply_curry():
    assert_equal(apply(add)([1, 2]), 3)
