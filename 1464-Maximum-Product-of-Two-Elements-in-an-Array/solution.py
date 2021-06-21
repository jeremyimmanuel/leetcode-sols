from typing import List


def maxProduct(nums: List[int]) -> int:
    # max_int = 0
    # max_int_2 = 0
    # max_int_idx = 0
    # for idx, num in enumerate(nums):
    #     if num >= max_int:
    #         max_int = num
    #         max_int_idx = idx

    # for idx, num in enumerate(nums):
    #     if idx == max_int_idx:
    #         continue
    #     max_int_2 = max(max_int_2, num)

    # return (max_int - 1) * (max_int_2 - 1)
    nums_reversed = sorted(nums, reverse=True)
    a, b = nums_reversed[0], nums_reversed[1]

    return (a - 1) * (b - 1)
