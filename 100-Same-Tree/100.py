class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if p == None and q == None:
        return True
    if p == None or q == None:
        return False
    
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)