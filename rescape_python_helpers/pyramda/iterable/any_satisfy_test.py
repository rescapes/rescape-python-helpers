from .any_satisfy import any_satisfy


def positive(x):
    return x > 0


def test_any_satisfy_nocurry():
    assert any_satisfy(positive, [-1, -2, 3])
    assert not any_satisfy(positive, [-1, -2, -3])


def test_any_satisfy_curry():
    assert any_satisfy(positive)([-1, -2, 3])
    assert not any_satisfy(positive)([-1, -2, -3])
