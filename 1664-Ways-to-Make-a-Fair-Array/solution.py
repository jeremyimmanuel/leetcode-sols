# 1. Find way to detect if array is fair

from typing import List


def isFair(nums: List[int]) -> bool:
    even, odd = 0, 0
    for i in range(len(nums)):
        if i % 2 == 0:
            even += nums[i]
        else:
            odd += nums[i]
    return odd == even


def waysToMakeFair(nums: List[int]) -> int:
    count = 0
    # brute force
    for i in range(len(nums)):
        nums_copy = nums.copy()
        nums_copy.pop(i)

        fair = isFair(nums_copy)
        if fair:
            count += 1
    return count
