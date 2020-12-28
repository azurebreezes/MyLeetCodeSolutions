# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        if not root:
            return 
        
        # cur_q=deque()
        nxt_q=deque()
        nxt_q.append(root)
        while nxt_q:
            cur_q=nxt_q
            nxt_q=deque()
            while cur_q:
                node=cur_q.popleft()
                if node:
                    if node.left:
                        nxt_q.append(node.left)
                    if node.right:
                        nxt_q.append(node.right)
                    if node==u:
                        if cur_q:
                            return cur_q.popleft()
                        return 
                        
                
            