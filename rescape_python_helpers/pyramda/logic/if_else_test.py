from .if_else import if_else
from rescape_python_helpers.pyramda.maths.inc import inc
from rescape_python_helpers.pyramda.maths.dec import dec
from rescape_python_helpers.pyramda.private.asserts import assert_equal


def positive(x):
    return x > 0


def test_if_else_nocurry():
    assert_equal(if_else(positive, inc, dec, 5), 6)
    assert_equal(if_else(positive, inc, dec, -5), -6)


def test_if_else_curry():
    inc_away_from_zero = if_else(positive, inc, dec)
    assert_equal(inc_away_from_zero(5), 6)
    assert_equal(inc_away_from_zero(-5), -6)
