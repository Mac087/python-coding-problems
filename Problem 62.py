# Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

# Do this faster than the naive method of repeated multiplication.

# For example, pow(2, 10) should return 1024.

def power(x, y):
    base = x
    exponent = y
    if y < 0:
        base = 1 / x
        exponent = -y
    coeff = 1
    while y > 1:
        if y % 2 == 0:
            base *= base
            y = y // 2
        else:
            coeff *= base
            base *= base
            y = (y - 1) // 2
    return coeff * base