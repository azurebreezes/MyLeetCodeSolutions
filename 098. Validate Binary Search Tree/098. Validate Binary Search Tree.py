# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def valid(node, up=math.inf, low=-math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= up:
                return False
        
            return valid(node.left, node.val, low) and valid(node.right, up, node.val)
        
        return valid(root)