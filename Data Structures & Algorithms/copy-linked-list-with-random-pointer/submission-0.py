"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = { None : None }
        curr = head
        # generate hash_map in one pass
        while curr:
            hash_map[curr] = Node(curr.val) # deep copy node
            curr = curr.next
        # generate deep copy in second pass
        curr = head
        while curr:
            copy = hash_map[curr]
            copy.next = hash_map[curr.next]
            copy.random = hash_map[curr.random]
            curr = curr.next
        return hash_map[head]
        


    