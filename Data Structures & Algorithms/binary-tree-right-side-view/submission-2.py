# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = [root]  # Start with the root in the queue.

        while queue:
            level_size = len(queue)  # Number of nodes in the current level.
            for i in range(level_size):
                node = queue.pop(0)  # Dequeue the front node.

                # Add children for the next level.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                # Check if this is the last node in the current level.
                if i == level_size - 1:
                    res.append(node.val)

        return res
            