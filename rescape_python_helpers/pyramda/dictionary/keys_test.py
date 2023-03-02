from .keys import keys
from rescape_python_helpers.pyramda.private.asserts import assert_iterables_equal


test_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}


def test_keys():
    assert_iterables_equal(keys(test_dict), set(["a", "c", "b"]))
