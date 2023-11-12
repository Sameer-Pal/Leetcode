# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        left= self.maxDepth(root.left)  # thsi will count recursio step when we godow 
        right= self.maxDepth(root.right)  # thsi will count recursio step when we godow 
        return 1 + max(left,right)        # bcz,  