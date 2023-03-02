from .isinstance import isinstance


def test_isinstance_nocurry():
    assert isinstance(str, "foo")


def test_isinstance_curry():
    assert isinstance(str)("foo")
