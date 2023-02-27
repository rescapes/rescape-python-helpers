from .apply import apply
from rescape_python_helpers.pyramda.private.asserts import assert_equal


def add(x, y):
    return x + y


def apply_nocurry_test():
    assert_equal(apply(add, [1, 2]), 3)


def apply_curry_test():
    assert_equal(apply(add)([1, 2]), 3)
