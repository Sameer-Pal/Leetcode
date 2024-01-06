# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node,currsum):
            if not node:
             return 0
            currsum= currsum*10+ node.val
            if not node.left and not node.right:
                return currsum
            lt = helper(node.left,currsum)
            rt = helper(node.right,currsum)
            return lt + rt
        return helper(root, 0)