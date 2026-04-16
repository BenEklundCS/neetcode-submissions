# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertRecursion(self, root):
        if root:
            temp = root.right
            root.right = root.left
            root.left = temp
            self.invertTree(root.left)
            self.invertTree(root.right)
        

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertRecursion(root)
        return root
        