from .ord import lt, gt, lte, gte


def test_lt():
    assert lt(3, 2)
    assert not lt(2, 3)
    assert not lt(3, 3)


def test_gt():
    assert gt(2, 3)
    assert not gt(3, 2)
    assert not gt(2, 2)


def test_lte():
    assert lte(3, 2)
    assert not lte(2, 3)
    assert lte(3, 3)


def test_gte():
    assert gte(2, 3)
    assert not gte(3, 2)
    assert gte(3, 3)
