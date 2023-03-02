from .pick import pick
from rescape_python_helpers.pyramda.private.asserts import assert_dicts_equal


test_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

expected_dict = {
    "b": 2,
    "d": 4
}


def test_pick_nocurry():
    assert_dicts_equal(pick(["b", "d"], test_dict), expected_dict)


def test_pick_curry():
    pickBD = pick(["b", "d"])
    assert_dicts_equal(pickBD(test_dict), expected_dict)
