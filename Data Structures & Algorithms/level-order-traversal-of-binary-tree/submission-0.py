# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderRecursion(self, root: Optional[TreeNode], res, level):
        if root:
            if len(res) == level:
                res.append([root.val])
            elif len(res) > level:
                res[level].append(root.val)
            self.levelOrderRecursion(root.left, res, level + 1)
            self.levelOrderRecursion(root.right, res, level + 1)
        return res


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level = 0
        return self.levelOrderRecursion(root, res, level)

        