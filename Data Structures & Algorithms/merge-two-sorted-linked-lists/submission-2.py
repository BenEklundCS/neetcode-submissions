# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = list1
        b = list2

        dummy = ListNode()
        current = dummy
        while a and b:
            if a.val < b.val:
                current.next = a
                a = a.next
                current = current.next
            else:
                current.next = b
                b = b.next
                current = current.next
        while a:
            current.next = a
            a = a.next
            current = current.next
        while b:
            current.next = b
            b = b.next
            current = current.next
        return dummy.next