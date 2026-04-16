# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # write it recursively.
        def recursion(root):
            # don't need to even update these
            nonlocal p
            nonlocal q

            if root.val < p.val and root.val < q.val:
                return recursion(root.right)
            elif root.val > p.val and root.val > q.val:
                return recursion(root.left)
            
            # base case
            else: 
                return root
        return recursion(root)
        
            
            

