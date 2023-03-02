from .dec import dec
from rescape_python_helpers.pyramda.private.asserts import assert_equal


def test_dec():
    assert_equal(dec(5), 4)
