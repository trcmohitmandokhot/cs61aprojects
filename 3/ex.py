from operator import mod, floordiv

def mydiv(n,d):
    """Return the quotient and remainder of dividing N by D.
    # Insert example here.
    >>> q_test, r_test = mydiv(55,7)
    >>> q_test
    7
    >>> r_test
    6
    """
    q = floordiv(n,d)
    r = mod(n,d)
    return q,r

# Test print statements
#print('The result of mydiv between numbers:', num, div, 'is: ')
#print('Quotient:',q_val)
#print('Remainder:',r_val)

def absval(x):
    """ Returns the absolute value of x
    >>> val_negx = abs(-5)
    >>> val_negx
    5
    >>> val_posx = abs(5)
    >>> val_posx
    5
    >>> val_zero= abs(0)
    >>> val_zero
    0
    """
    if x>=0:
        return x
    else:
        return -1*x



