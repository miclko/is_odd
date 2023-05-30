from is_even import is_even

def is_odd(x):
    """ Is odd function checks for odd integers, using even function
    x: integer
    output:
    true if x is odd
    false if x is even
    Exception if no integer
    """
    evenCheck = false;
    try:
        evenCheck = is_even(x)
    except:   
        raise('Exception')
    return not evenCheck    
    




assert is_even is not None

assert is_odd.__doc__ is not None

exception_created = False;
try:
    is_odd('asgaerw')
except:
    exception_created = True
    
assert exception_created     