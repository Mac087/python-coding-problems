# Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards 
# represented as an array using only swaps.

# It should run in O(N) time.

# Hint: Make sure each one of the 52! permutations of the deck is equally likely.

def shuffle(arr):
    n = len(arr)
    for i in range(n - 1):
        j = randint(i, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr