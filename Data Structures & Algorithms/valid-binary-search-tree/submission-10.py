# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBSTRecursion(self, root: Optional[TreeNode], left_bound: int, right_bound: int) -> bool:
        if not root:
            return True
        if (left_bound is None or left_bound < root.val) and (right_bound is None or root.val < right_bound):
            return self.isValidBSTRecursion(root.left, left_bound, root.val) and self.isValidBSTRecursion(root.right, root.val, right_bound)
        return False


    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.isValidBSTRecursion(root, None, None)

        