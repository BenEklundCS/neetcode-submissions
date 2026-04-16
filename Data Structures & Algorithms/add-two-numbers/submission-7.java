/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ptr1 = l1;
        ListNode ptr2 = l2;

        ListNode dummy = new ListNode(0); // ptr to nothing
        ListNode curr = dummy;

        int carry = 0;

        while (ptr1 != null || ptr2 != null || carry > 0) {
            int l = ptr1 != null ? ptr1.val : 0;
            int r = ptr2 != null ? ptr2.val : 0;
            int rawValue = l + r + carry;

            carry = rawValue / 10; 
            int value = rawValue % 10;

            curr.next = new ListNode(value);

            curr = curr.next;
            ptr1 = ptr1 != null ? ptr1.next : null;
            ptr2 = ptr2 != null ? ptr2.next : null;
        }

        return dummy.next;
    }
}
