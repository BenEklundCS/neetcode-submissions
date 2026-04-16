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
        while a and b:
            s = a.val + b.val
            print(s % 10 + carry)
            if s % 10 + carry < 10:
                curr.next = ListNode(s % 10 + carry)
                carry = s // 10
            a = a.next
            b = b.next
            curr = curr.next

        print("Finished adding main while loop")
        print(carry)

        while a:
            curr.next = ListNode((a.val + carry) % 10)
            carry = (a.val + carry) // 10
            a = a.next
            curr = curr.next
        while b:
            curr.next = ListNode((b.val + carry) % 10)
            carry = (b.val + carry) // 10
            b = b.next
            curr = curr.next

        if carry > 0:
            curr.next = ListNode(carry)

        return dummy.next

