from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
def constructMaximumBinaryTree(nums: List[int]) -> TreeNode:
    # base case 
    # if list if empty return None
    if len(nums) == 0:
        return None

    if len(nums) == 1:
        return TreeNode(nums[0])
    
    # get max val
    rootVal = max(nums)

    # set as root
    root = TreeNode(rootVal)

    # get idx of rootVal
    maxIdx = nums.index(rootVal)

    # divide left and right
    left = nums[0:maxIdx]
    right = nums[maxIdx:len(nums)]

    root.left = constructMaximumBinaryTree(left)
    root.right = constructMaximumBinaryTree(right)

    return root
'''

def constructMaximumBinaryTree(nums: List[int]) -> TreeNode:
    construct(nums, 0, len(nums))

def construct(nums: List[int], l: int, r: int) -> TreeNode:
    if l == r:
        return None
    maxIdx: int = getMaxIdx(nums, l, r)
    root: TreeNode = TreeNode(nums[maxIdx])
    root.left = construct(nums, l, maxIdx)
    root.right = construct(nums, maxIdx + 1, r)

    return root

def getMaxIdx(nums: List[int], l: int, r: int) -> int:
    ans = l
    for i in range(l, r):
        if nums[ans] < nums[i]:
            ans = i
    return ans

def test1():
    nums = [3, 2, 1, 6, 0, 5]
    

def main():
    pass

if __name__ == "__main__":
    main()
