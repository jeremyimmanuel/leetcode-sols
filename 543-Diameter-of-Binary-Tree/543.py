class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def diameterOfBinaryTree(root: TreeNode) -> int:
    return getHeight(root.right) + getHeight(root.left)

def getHeight(root: TreeNode) -> int:
    if root == None:
        return 0
    
    return 1 + max(getHeight(root.left), getHeight(root.right))

