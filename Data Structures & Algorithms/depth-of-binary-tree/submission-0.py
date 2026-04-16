# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def getMaxDepth(self, root: Optional[TreeNode], max_depth) -> int:
        if root and (root.left or root.right):
            max_depth += 1
            left_depth = self.getMaxDepth(root.left, max_depth)
            right_depth = self.getMaxDepth(root.right, max_depth)
            return left_depth if left_depth > right_depth else right_depth
        return max_depth


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = 1
        return self.getMaxDepth(root, max_depth)

