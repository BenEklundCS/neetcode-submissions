# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0
        def dfs(root):
            nonlocal longest
            if root:
                l = dfs(root.left)
                r = dfs(root.right)
                longest = max(l + r, longest)
                return max(l + 1, r + 1)
            return 0
        dfs(root)
        return longest
        