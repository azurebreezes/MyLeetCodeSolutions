# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        head = point = ListNode(0)
        for i in lists:
            while i:
                nodes.append(i.val)
                i = i.next
        
        for i in sorted(nodes):
            point.next = ListNode(i)
            point = point.next
        
        return head.next
            