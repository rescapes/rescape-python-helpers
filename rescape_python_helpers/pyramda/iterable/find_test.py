from .find import find
from rescape_python_helpers.pyramda.private.asserts import assert_equal


def positive(x):
    return x > 0


def test_find_nocurry():
    assert_equal(find(positive, [-2, -1, 0, 1, 2]), 1)


def test_find_curry():
    assert_equal(find(positive)([-2, -1, 0, 1, 2]), 1)
