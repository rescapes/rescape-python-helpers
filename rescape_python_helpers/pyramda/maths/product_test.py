from .product import product
from rescape_python_helpers.pyramda.private.asserts import assert_equal


def test_product():
    assert_equal(product([2, 3, 5]), 30)
