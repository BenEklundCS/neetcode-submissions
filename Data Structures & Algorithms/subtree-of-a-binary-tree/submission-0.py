# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    # Try using a same tree algorithm to determine this
    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if (a and b):
            if (a.val == b.val):
                if (self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)):
                    return True
        elif (not a and not b):
            return True
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root, subRoot):
            return True
        if root.left and root.right:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        elif root.left:
            return self.isSubtree(root.left, subRoot)
        elif root.right:
            return self.isSubtree(root.right, subRoot)
        return False
        
        