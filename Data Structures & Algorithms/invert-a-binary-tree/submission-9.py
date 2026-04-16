# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recursion(node):
            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left:
                recursion(node.left)
            if node.right:
                recursion(node.right)

        if root:
            recursion(root)
        return root