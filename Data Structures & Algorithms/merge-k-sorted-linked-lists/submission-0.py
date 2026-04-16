# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while True: # loop infinitely
            lowest_node = -1 # start with an invalid index
            for i, node in enumerate(lists):
                if not node: # list is already done processing
                    continue
                if lowest_node == -1 or lists[lowest_node].val > node.val:
                    # we have found a valid lowest node
                    lowest_node = i
            if lowest_node == -1:
                break # infinite loop ends, as there are no more valid nodes
            curr.next = lists[lowest_node]
            curr = curr.next
            lists[lowest_node] = lists[lowest_node].next
        return dummy.next
