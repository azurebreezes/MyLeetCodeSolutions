# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        v1=0
        v2=0
        carrier=0
        pseudoHead=ListNode(0,None)
        
        newNode=ListNode(0)
        pseudoHead.next=newNode
        
        while l1 or l2:
            if l1:
                v1=l1.val
                l1=l1.next
            else:
                v1=0
            if l2:
                v2=l2.val
                l2=l2.next
            else:
                v2=0
            
            remainder=(v1+v2)%10
            
            newNode.next=ListNode()
            newNode.next.val=(remainder+carrier)%10
            
            carrier=(v1+v2+carrier)//10
            newNode=newNode.next
        if carrier>0:
            newNode.next=ListNode()
            newNode.next.val=carrier
            newNode=newNode.next
        return pseudoHead.next.next

            