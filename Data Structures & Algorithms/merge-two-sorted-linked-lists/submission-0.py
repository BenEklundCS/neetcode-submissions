# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = list1
        b = list2

        # Edge cases, num nodes == 0 in either list
        if (a == None):
            return b
        elif (b == None):
            return a

        res = None

        if a.val < b.val:
            res = ListNode(a.val)
            a = a.next
        else:
            res = ListNode(b.val)
            b = b.next

        itr = res

        # Main algorithm for splicing
        while a is not None and b is not None:
            # Create a new listnode at the current itr
            if a.val < b.val:
                itr.next = ListNode(a.val)
                a = a.next
            else:
                itr.next = ListNode(b.val)
                b = b.next
            itr = itr.next

        # Edge case loops for leftovers or uneven lengths
        while (a != None):
            itr.next = ListNode(a.val)
            a = a.next
            itr = itr.next

        while (b != None):
            itr.next = ListNode(b.val)
            b = b.next
            itr = itr.next

        return res

            
