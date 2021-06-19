"""
Function Generalization.
First using numbers/arguments/parameters that can be generalized.
Next using the mathematics that may be generalized. 
"""
from math import pi
from operator import mul,truediv

def area(x, k_shape):
    """
    Fundamental Area Function
    """
    assert x>0, 'Length should be positive'
    return x*x*k_shape

def area_square(x):
    """ Area of square with side x."""
    return area(x,1)

def area_circle(x):
    """ Area of circle with radius x."""
    return area(x,pi)

"""
Return the sum of five terms. 
The individual terms can look different.
"""
def cubed(k):
    return pow(k,3)

def identity(k):
    return k

def unique(k):
    return truediv(8,mul((4*k-3),(4*k-1)))

def sumterms(N,kind):
    """
    Returns the sum of first N terms of a certain kind
    The kind of terms can be defined seperately
    """
    i = 1
    k = 0
    while i <= N:
        k = kind(i) + k
        i+= 1
    return k


def sum5terms():
    """
    Returns sum of first five terms from k=1,5
    >>> sum5terms()
    15
    """
    return sumterms(5,identity)

def sum5terms_cubed():
    """
    Returns sum of first five terms from k=1,5 cubed
    >>> sum5terms_cubed()
    225
    """
    return sumterms(5,cubed)

def sum5terms_unique():

    """
    Returns sum of first five terms from k=1,5 with a unique function applied to it.
    >>> sum5terms_unique()
    3.04
    """
    a = sumterms(5,unique)
    return a

