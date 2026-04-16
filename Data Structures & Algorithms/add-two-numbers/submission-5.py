# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = l1
        b = l2
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        # addition algorithm (add until a, b, and carry bit are expended)
        while a or b or carry:
            a_val = a.val if a else 0
            b_val = b.val if b else 0
            s = a_val + b_val + carry
            val = s % 10
            carry = s // 10
            curr.next = ListNode(val)
            # Move pointers forward
            curr = curr.next
            a = a.next if a else None
            b = b.next if b else None
        return dummy.next

