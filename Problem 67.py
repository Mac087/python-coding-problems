# Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

# Write a function to simulate an unbiased coin toss.


from random import random

BIAS = 0.66

def toss_biased():
    return random() > BIAS

def toss_fair():
    t1, t2 = toss_biased(), toss_biased()
    if t1 and not t2:
        return True
    elif not t1 and t2:
        return False
    else:
        return toss_fair()