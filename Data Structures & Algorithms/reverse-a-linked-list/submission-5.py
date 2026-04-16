# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def recursion(head, prev):
            if not head:
                return prev
            
            temp = head.next
            head.next = prev

            return recursion(temp, head)


        return recursion(head, None)

