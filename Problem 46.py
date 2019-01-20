# Using a function rand5() that returns an integer from 1 to 5 (inclusive) 
# with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).

def rand7():
    r1, r2 = rand5(), rand5()
    if r2 <= 3:
        return r1
    elif r2 == 4:
        if r1 <= 3:
            return 6
        else:
            return rand7()
    else: # r2 == 5
        if r1 <= 3:
            return 7
        else:
            return rand7()