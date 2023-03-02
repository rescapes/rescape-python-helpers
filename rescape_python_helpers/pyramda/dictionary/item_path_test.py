from .item_path import item_path
from rescape_python_helpers.pyramda.private.asserts import assert_equal


test_dict = {
    "a": {
        "b": {
            "c": "foo"
        }
    }
}


def test_item_path_nocurry():
    assert_equal(item_path(["a", "b", "c"], test_dict), "foo")


def test_item_path_curry():
    get_abc = item_path(["a", "b", "c"])
    assert_equal(get_abc(test_dict), "foo")
