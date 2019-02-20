# An sorted array of integers was rotated an unknown number of times.

# Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

# You can assume all the integers in the array are unique.

def shifted_array_search(lst, num):
    # First, find where the breaking point is in the shifted array
    i = len(lst) // 2
    dist = i // 2
    while True:
        if lst[0] > lst[i] and lst[i - 1] > lst[i]:
            break
        elif dist == 0:
            break
        elif lst[0] <= lst[i]:
            i = i + dist
        elif lst[i - 1] <= lst[i]:
            i = i - dist
        else:
            break
        dist = dist // 2

    # Now that we have the bottom, we can do binary search as usual,
    # wrapping around the rotation.
    low = i
    high = i - 1
    dist = len(lst) // 2
    while True:
        if dist == 0:
            return None

        guess_ind = (low + dist) % len(lst)
        guess = lst[guess_ind]
        if guess == num:
            return guess_ind

        if guess < num:
            low = (low + dist) % len(lst)
        if guess > num:
            high = (len(lst) + high - dist) % len(lst)

        dist = dist // 2