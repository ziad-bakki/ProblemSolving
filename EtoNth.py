import math


def NthE(n):
    """
    returns E up to N decimal places
    """
    e = str(math.e)
    return e[:n+2]
