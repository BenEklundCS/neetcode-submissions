# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        stack = []
        # Store linkedlist in stack memory
        while curr:
            stack.append(curr.val)
            curr = curr.next
        # Pop it to reverse the order
        dummy = ListNode()
        curr = dummy
        while stack:
            curr.next = ListNode(stack.pop())
            curr = curr.next
        return dummy.next            

        
