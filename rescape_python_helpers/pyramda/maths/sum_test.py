from .sum import sum
from rescape_python_helpers.pyramda.private.asserts import assert_equal


def test_sum():
    assert_equal(sum([1, 2, 3]), 6)
