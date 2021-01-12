# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0
        new_node = ListNode()
        pseudo_head = ListNode()
        pseudo_head.next = new_node
        
        while l1 and l2 :
            sum_ = sum([l1.val,l2.val,carry])
            new_node.val = sum_%10
            carry = sum_//10

            l1,l2 = l1.next,l2.next
                    
            if l1 or l2 or carry==1:
                new_node.next = ListNode(1)
            else:
                new_node.next = None
            new_node = new_node.next
            
        while l1:
            sum_ = l1.val+carry
            new_node.val = sum_%10
            carry = sum_//10
            l1 = l1.next
            if l1 or carry == 1:
                new_node.next = ListNode(1,None)
            new_node = new_node.next
            
        while l2:
            sum_ = l2.val+carry
            new_node.val = sum_%10
            carry = sum_//10
            l2 = l2.next
            if l2 or carry == 1:
                new_node.next = ListNode(1,None)
            new_node = new_node.next

        return pseudo_head.next
            
        