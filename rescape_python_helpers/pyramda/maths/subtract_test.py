from .subtract import subtract
from rescape_python_helpers.pyramda.private.asserts import assert_equal


def subtract_nocurry_test():
    assert_equal(subtract(4, 3), 1)


def subtract_curry_test():
    assert_equal(subtract(4)(3), 1)
