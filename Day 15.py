# ----------------Problem--------------------
# This problem was asked by Facebook.

# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

# ------------Solution---------------

# Naively, we could process the stream and store all the elements we encounter in a list, find its size, and pick a random element from [0, size - 1]. The problem with this approach is that it would take O(N) space for a large N.



import random

def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if random.randint(1, i + 1) == 1:
            random_element = e
    return random_element