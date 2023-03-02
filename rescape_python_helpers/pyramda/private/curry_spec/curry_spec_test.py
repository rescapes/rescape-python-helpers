from functools import partial, wraps
from .curry_spec import *
from .make_func_curry_spec import make_func_curry_spec
from ..asserts import \
    assert_equal, \
    assert_not_in_domain


def assert_isinstance(type, v):
    assert isinstance(v, type)


def test_curry_spec_creation():
    assert_isinstance(CurrySpec, CurrySpec(['x', 'y', 'z'], {'y': 5}))


def test_num_args():
    two_posn_three_kwarg_arg_values = ArgValues(
        [1, 2],
        {'foo': 5, 'bar': 7, 'baz': 10}
    )
    assert_equal(num_args(two_posn_three_kwarg_arg_values), 5)
