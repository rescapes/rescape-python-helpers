from .negate import negate
from rescape_python_helpers.pyramda.private.asserts import assert_equal


def test_negate():
    assert_equal(negate(5), -5)
