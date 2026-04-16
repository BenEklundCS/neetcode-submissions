# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recurse(p, q):
            # base case
            if not p and not q:
                return True
            if not p and q or p and not q:
                return False
            # recursive case
            if p.val != q.val:
                return False
            else:
                return recurse(p.left, q.left) and recurse(p.right, q.right)
        
        return recurse(p, q)
        