import math

"""
returns E up to N decimal places
"""
def NthE(n):
    e = str(math.e)
    return e[:n+2]
