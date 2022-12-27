def main(a, b):
    '''find the floor division of a and b and return it.
    
    Args:
        a (int): a number
        b (int): a number
        
    Returns:
        int: the result.
    '''
    x = int(a) // int(b)
    return x

y = main(11, 2)
print(y)