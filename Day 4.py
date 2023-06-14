# --------------Problem-------------
# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

#------------Solution----------


def first_missing_positive(nums):
    if not nums:
        return 1
    for i, num in enumerate(nums):
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
            if nums[i] == nums[v - 1]:
                break
    for i, num in enumerate(nums, 1):
        if num != i:
            return i
    return len(nums) + 1

# Another way we can do this is by adding all the numbers to a set, and then use a counter initialized to 1. Then continuously increment the counter and check whether the value is in the set.

def first_missing_positive(nums):
    s = set(nums)
    i = 1
    while i in s:
        i += 1
    return i

# This is much simpler, but runs in O(N) time and space, whereas the previous algorithm uses no extra space.