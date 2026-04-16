# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head and head.next:
            slow = head
            fast = head.next

            while slow and slow.next and fast and fast.next and fast.next.next:
                
                if slow == fast:
                    return True
                
                slow = slow.next
                fast = fast.next.next


        return False

        