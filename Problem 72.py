# Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() 
# that returns an integer from 1 to 5 (inclusive).

def rand5():
    r = rand7()
    if 1 <= r <= 5:
        return r
    return rand5()