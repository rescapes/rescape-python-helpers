from rescape_python_helpers.pyramda.function.curry import curry


@curry
def complement(p, v):
    """
    Only works on unary functions
    :param p:
    :param v:
    :return:
    """
    return not p(v)
