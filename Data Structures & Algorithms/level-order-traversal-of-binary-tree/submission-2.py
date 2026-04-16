# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = []
        # use bfs and a queue for level order traversal
        queue = [root]

        while queue:
            sub_res = []

            for node in queue:
                sub_res.append(node.val)
            res.append(sub_res)

            level_length = len(queue)
            for i in range(level_length): # iterate over the queue to remove all nodes, and add the children
                node = queue.pop(0) # pop current node
                # add its children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res

