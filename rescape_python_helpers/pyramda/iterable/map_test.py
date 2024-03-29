from .map import map
from rescape_python_helpers.pyramda.private.asserts import assert_iterables_equal


def add1(x):
    return x + 1


def test_map_nocurry():
    assert_iterables_equal(map(add1, [1, 2, 3]), [2, 3, 4])


def test_map_curry():
    assert_iterables_equal(map(add1)([1, 2, 3]), [2, 3, 4])
