# Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. 
# Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

# You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. 
# No string in the list has a length of more than 10.

def break(s, k):
    words = s.split()

    if not words:
        return []

    current = []
    all = []

    for i, word in enumerate(words):
        if length(current + [word]) <= k:
            current.append(word)
        elif length([word]) > k:
            return None
        else:
            all.append(current)
            current = [word]
    all.append(current)

    return all

def length(words):
    if not words:
        return 0
    return sum(len(word) for word in words) + (len(words) - 1)