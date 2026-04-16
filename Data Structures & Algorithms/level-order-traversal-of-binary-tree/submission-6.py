# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # return empty array when passed no Node
        if not root:
            return []

        # define empty result array for return at end of function
        result = []
        # "bfs processing queue" add root to queue for processing
        queue = [root]

        # while nodes exist in the queue, or are "ready for processing"
        while queue:
            # begin building the result for this sublevel
            sub_result = []
            # get the length of the sublevel from the processing queue
            level_length = len(queue)

            # iterate over the length of the sublevel
            for i in range(level_length):
                # pop each node in order [1, 2, 3] -> pop 1, pop 2, pop 3
                node = queue.pop(0)
                # append the node value to the subresult ([1, 2, 3])
                sub_result.append(node.val)

                # if nodes exist, add to the processing queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # append the result to the subresult, then wrap back to process the next list in the queue
            result.append(sub_result)
        return result 
        

            