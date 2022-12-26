from math import sqrt

def main(a):
    '''find the square root of a number and return it.
    
    Args:
        a (int): a number
        
    Returns:
        float: the absolute value.
    '''
    x = sqrt(a)
    return x

y = main(81)
print(y)