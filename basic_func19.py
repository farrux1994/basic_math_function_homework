def main(a, b):
    '''find the absolute value of the difference between a and b. Return it.
    
    Args:
        a (int): a number
        b (int): a number
        
    Returns:
        int: the result.
    '''
    x = int(a) - int(b)
    return x

y = main(4, 11)
print(abs(y))