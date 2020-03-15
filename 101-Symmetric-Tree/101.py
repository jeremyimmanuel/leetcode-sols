class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root: TreeNode) -> bool:
    '''
    Two trees are mirror reflections of each other if:
        1. Their roots are the same
        2. right subtrees == left subtrees
    '''

    return isReflection(root, root)
    

def isReflection(left: TreeNode, right: TreeNode) -> bool:
    if left == None and right == None:
        return True
    if left == None or right == None:
        return False

    return (left.val == right.val) and isReflection(left.right, right.left) and isReflection(right.left, left.right)

def main():
    pass

if __name__ == "__main__":
    main()


