# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Append values to this dummy node
        dummy = ListNode(0)
        curr = dummy
        # Two-pointer algorithm, while l1 and l2 both exist I'll move forward adding them together
        a = l1
        b = l2
        # Addition will require a carry bit
        carry = 0
        # Both pointers have numbers to add
        while a or b or carry:
            v1 = a.val if a else 0
            v2 = b.val if b else 0
            s = v1 + v2 + carry
            carry = s // 10
            val = s % 10
            curr.next = ListNode(val)
            a = a.next if a else None
            b = b.next if b else None
            curr = curr.next

        return dummy.next

