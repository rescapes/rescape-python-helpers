from .min import min
from rescape_python_helpers.pyramda.private.asserts import assert_equal


def test_min():
    assert_equal(min([3, 1, 4, 2]), 1)
