# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_map = {}
        current = head
        idx = 0

        # Store each node in a dictionary with its index as the key
        while current:
            node_map[idx] = current
            current = current.next
            idx += 1

        list_length = len(node_map)
        target = list_length - n  # Index of the node to remove

        # Handle case where the first node needs to be removed
        if target == 0:
            return head.next  # Skip the head

        # Handle general case by adjusting the `next` pointer of the previous node
        previous_node = node_map[target - 1]
        node_to_remove = node_map[target]

        # Adjust the pointers to remove the target node
        previous_node.next = node_to_remove.next

        return head
