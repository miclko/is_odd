#is even function


def is_even(x):
    """Function for checking evenness of integers
    Input: x integer
    output:
    true if x  even
    false if x odd
    raise exception if not an integer 
    """    
    if not isinstance(x,int):
        raise Exception('not an integer')
    if x % 2 == 0:
        return True
    else:
        return False    


assert is_even.__doc__ 

has_raised_exception = False
try:
    is_even('3sajnk')
except:
    has_raised_exception = True
    
assert has_raised_exception    


assert is_even(1) == False
assert is_even(2) == True 
