from .add import add
from rescape_python_helpers.pyramda.private.asserts import assert_equal


def test_add_nocurry():
    assert_equal(add(1, 2), 3)


def test_add_curry():
    assert_equal(add(1)(2), 3)
