# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and q):
            if (p.val == q.val):
                if (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)):
                    return True

        # Catches both the case where 
        #   p = []
        #   q = []
        # as well as all cases where we run out of items to iterate over!
        elif (not p and not q):
            return True

        return False
        