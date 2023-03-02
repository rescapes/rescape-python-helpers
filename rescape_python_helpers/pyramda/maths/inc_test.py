from .inc import inc
from rescape_python_helpers.pyramda.private.asserts import assert_equal


def test_inc():
    assert_equal(inc(5), 6)
