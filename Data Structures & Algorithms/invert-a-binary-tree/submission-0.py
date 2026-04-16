# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Descend the tree and swap nodes
    def recursivelySwapNodes(self, root):
        if root:
            if root.left:
                self.recursivelySwapNodes(root.left)
            if root.right:
                self.recursivelySwapNodes(root.right)
        
            temp = root.left
            root.left = root.right
            root.right = temp

    # Invert tree and return the root node
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        main_root = root
        self.recursivelySwapNodes(root)
        return main_root



        