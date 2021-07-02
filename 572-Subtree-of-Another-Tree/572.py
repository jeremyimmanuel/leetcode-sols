"""
Solution from leetcode
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSubtree(s: TreeNode, t: TreeNode) -> bool:
    return traverse(s, t)


# DFS solution
def equals(s: TreeNode, t: TreeNode) -> bool:
    # if both are None
    if s == None and t == None:
        return True

    # if either is None
    if s == None or t == None:
        return False

    return s.val == t.val and equals(s.left, t.left) and equals(s.right, t.right)


def traverse(s: TreeNode, t: TreeNode) -> bool:
    # if None return false
    if s == None:
        return False

    compareThisTree = equals(s, t)
    compareLeftSubtree = traverse(s.left, t)
    compareRightSubtree = traverse(s.right, t)

    return compareThisTree or compareLeftSubtree or compareRightSubtree


def main():
    pass


if __name__ == "__main__":
    pass
