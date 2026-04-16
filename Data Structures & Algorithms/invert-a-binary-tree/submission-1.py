# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursivelySwapNodes(self, root: Optional[TreeNode], parent: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            # Swap the nodes (even if they're None)
            temp = root.left
            root.left = root.right
            root.right = temp
            # Recursively swap the children
            self.recursivelySwapNodes(root.left, parent)
            self.recursivelySwapNodes(root.right, parent)
        return parent
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.recursivelySwapNodes(root, root)
        
            
            