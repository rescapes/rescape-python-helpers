from .cons import cons
from rescape_python_helpers.pyramda.private.asserts import assert_iterables_equal


def test_cons_nocurry():
    assert_iterables_equal(cons(1, [2, 3]), [1, 2, 3])


def test_cons_curry():
    assert_iterables_equal(cons(1)([2, 3]), [1, 2, 3])
