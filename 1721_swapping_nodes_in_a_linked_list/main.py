# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # First pass to get the total number of nodes
        dummy = head
        tot = 0
        while dummy:
            dummy = dummy.next
            tot += 1
            
        index1 = k
        index2 = tot - k + 1
        
        # Second pass to get the nodes for swapping
        dummy = head
        counter = 1
        while dummy:
            if counter == k:
                node1 = dummy
            if counter == index2:
                node2 = dummy
            dummy = dummy.next
            counter += 1
        # Swap the node values
        node1.val, node2.val = node2.val, node1.val
        return head
        
            
            