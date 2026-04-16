# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def dfs(root):
            # base case
            if not root:
                return 0

            # recursive step
            nonlocal isBalanced
            r = dfs(root.right)
            l = dfs(root.left)
            if abs(r - l) > 1:
                isBalanced = False
            return max(r, l) + 1

        dfs(root)
        return isBalanced

        