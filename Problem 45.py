# We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. 
# That is, a smaller element appears after a larger element.

# Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

# You may assume each element in the array is distinct.

# For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). 
# The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

def count_inversions(arr):
    count, _ = count_inversions_helper(arr)
    return count

def count_inversions_helper(arr):
    if len(arr) <= 1:
        return 0, arr
    mid = len(arr) // 2
    a = arr[:mid]
    b = arr[mid:]
    left_count, left_sorted_arr = count_inversions_helper(a)
    right_count, right_sorted_arr = count_inversions_helper(b)
    between_count, sorted_arr = merge_and_count(left_sorted_arr, right_sorted_arr)
    return left_count + right_count + between_count, sorted_arr

def merge_and_count(a, b):
    count = 0
    sorted_arr = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            sorted_arr.append(a[i])
            i += 1
        elif a[i] > b[j]:
            sorted_arr.append(b[j])
            count += len(a) - i
            j += 1
    sorted_arr.extend(a[i:])
    sorted_arr.extend(b[j:])
    return count, sorted_arr