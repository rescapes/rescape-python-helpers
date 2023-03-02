from unittest import TestCase

from .all_satisfy import all_satisfy


def positive(x):
    return x > 0


class TestAllSatisfy(TestCase):

    def test_all_satisfy_nocurry(self):
        assert all_satisfy(positive, [1, 2, 3])
        assert not all_satisfy(positive, [1, -2, 3])

    def test_all_satisfy_curry(self):
        assert all_satisfy(positive)([1, 2, 3])
        assert not all_satisfy(positive)([1, -2, 3])
