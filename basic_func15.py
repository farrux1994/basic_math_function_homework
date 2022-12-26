def main(a, b):
    '''Find the remainder when a is divided by b and return it.
    
    Args:
        a (int): a number
        b (int): a number
        
    Returns:
        int: the result.
    '''
    x = int(a) % int(b)
    return x

y = main(10, 3)
print(y)