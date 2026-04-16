# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while True:
            min_node = -1
            # find the real min_node
            for i, node in enumerate(lists):
                if not node:
                    continue
                if min_node == -1 or lists[min_node].val > node.val:
                    min_node = i
            if min_node == -1:
                break
            else:
                curr.next = lists[min_node]
                lists[min_node] = lists[min_node].next
                curr = curr.next
        return dummy.next 