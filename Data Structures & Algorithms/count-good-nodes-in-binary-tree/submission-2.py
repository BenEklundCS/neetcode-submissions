# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countGoodNodes(root, curr_max):
            if root:
                curr_max = max(root.val, curr_max)
                l = countGoodNodes(root.left, curr_max)
                r = countGoodNodes(root.right, curr_max)
                res = 1 if root.val >= curr_max else 0
                return l + r + res
            return 0
        return countGoodNodes(root, root.val)