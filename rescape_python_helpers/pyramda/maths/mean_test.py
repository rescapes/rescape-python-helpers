from .mean import mean
from rescape_python_helpers.pyramda.private.asserts import assert_equal


def mean_test():
    assert_equal(mean([3, 5, 7]), 5)
    assert_equal(mean([5, 7, 3]), 5)
