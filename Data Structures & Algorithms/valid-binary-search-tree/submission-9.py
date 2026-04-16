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

        if left_bound is not None and root.val <= left_bound:
            return False

        if right_bound is not None and root.val >= right_bound:
            return False
        
        return self.isValidBSTRecursion(root.left, left_bound, root.val) and self.isValidBSTRecursion(root.right, root.val, right_bound)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTRecursion(root, None, None)

        