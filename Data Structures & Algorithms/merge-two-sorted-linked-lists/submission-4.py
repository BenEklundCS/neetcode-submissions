# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_ptr = list1
        list2_ptr = list2

        dummy = ListNode(0)
        curr = dummy

        while list1_ptr and list2_ptr:
            # which value should go next in our "new list?"
            if list1_ptr.val < list2_ptr.val:
                curr.next = list1_ptr
                list1_ptr = list1_ptr.next
            else:
                curr.next = list2_ptr
                list2_ptr = list2_ptr.next
            curr = curr.next

        while list1_ptr:
            curr.next = list1_ptr
            list1_ptr = list1_ptr.next
            curr = curr.next
        
        while list2_ptr:
            curr.next = list2_ptr
            list2_ptr = list2_ptr.next
            curr = curr.next

        return dummy.next

            


        