# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getTreeInOrder(self, root: Optional[TreeNode], lst: List[int]) -> List[int]:
        if root:
            self.getTreeInOrder(root.left, lst)
            lst.append(root.val)
            self.getTreeInOrder(root.right, lst)
        return lst
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        lst = self.getTreeInOrder(root, arr)
        return lst[k - 1]
