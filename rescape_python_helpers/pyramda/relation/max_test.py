from .max import max
from rescape_python_helpers.pyramda.private.asserts import assert_equal


def test_max():
    assert_equal(max([1, 3, 4, 2]), 4)
