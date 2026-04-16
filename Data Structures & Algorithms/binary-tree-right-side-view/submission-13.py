# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level order traversal where you only care about the "last" of each level I think
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            sub_res = []
            length = len(queue)

            for i in range(length):
                node = queue.pop(0)

                sub_res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                print(sub_res)

            res.append(sub_res.pop())

        return res

