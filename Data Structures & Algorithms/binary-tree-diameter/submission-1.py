# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_diameter = 0  # To store the maximum diameter

    def diameterRecursion(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # Base case: height of a null subtree is 0

        # Recursively find the height of the left and right subtrees
        left_height = self.diameterRecursion(root.left)
        right_height = self.diameterRecursion(root.right)

        # Update the maximum diameter if the current path is larger
        self.max_diameter = max(self.max_diameter, left_height + right_height)

        # Return the height of the current subtree
        return 1 + max(left_height, right_height)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameterRecursion(root)
        return self.max_diameter
