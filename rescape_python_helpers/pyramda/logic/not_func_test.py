from .not_func import not_func


def test_not_func():
    assert not not_func(True)
    assert not_func(False)
