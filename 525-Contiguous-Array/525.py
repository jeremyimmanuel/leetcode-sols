def findMaxLength(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    maxLen = 0
    # brute force O(n^2)
    for i in range(len(nums)):
        zeroes, ones = 0, 0
        for j in range(i, len(nums)):
            if nums[j] == 0:
                zeroes += 1
            elif nums[j] == 1:
                ones += 1
            if zeroes == ones:
                maxLen = max(maxLen, j - i + 1)
    
    return maxLen

def main():
    pass

if __name__ == "__main__":
    main()