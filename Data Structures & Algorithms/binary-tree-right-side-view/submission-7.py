# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def bfs(root):
            nonlocal res
            queue = [root]
            while queue:
                # get the length of the current level
                current_level_length = len(queue)
                for i in range(current_level_length):
                    node = queue.pop(0) # get the next node to process
                    # add its children to the queue for LATER processing
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    if i == current_level_length - 1: # we're at the rightmost node in the level
                        res.append(node.val)
        if root:
            bfs(root)
        return res