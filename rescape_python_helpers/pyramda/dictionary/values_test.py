from .values import values
from rescape_python_helpers.pyramda.private.asserts import assert_iterables_equal


test_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}


def test_values():
    assert_iterables_equal(set(values(test_dict)), set([1, 3, 2]))
