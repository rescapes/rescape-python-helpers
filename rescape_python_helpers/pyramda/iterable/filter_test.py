from .filter import filter
from rescape_python_helpers.pyramda.private.asserts import assert_iterables_equal


def positive(x):
    return x > 0


def test_filter_nocurry():
    assert_iterables_equal(filter(positive, [2, -1, 0, 3, -2]), [2, 3])


def test_filter_curry():
    assert_iterables_equal(filter(positive)([2, -1, 0, 3, -2]), [2, 3])
