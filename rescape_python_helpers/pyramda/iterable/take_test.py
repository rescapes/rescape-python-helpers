from .take import take
from rescape_python_helpers.pyramda.private.asserts import assert_iterables_equal


def test_take_nocurry():
    assert_iterables_equal(take(2, [1, 2, 3, 4]), [1, 2])


def test_take_curry():
    assert_iterables_equal(take(2)([1, 2, 3, 4]), [1, 2])
