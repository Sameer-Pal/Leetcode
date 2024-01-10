# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = float("-inf")   

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0
            left = max(0, helper(node.left))
            right = max(0, helper(node.right))
            path = left+right+node.val
            self.ans = max(path, self.ans)
            return max(left, right) + node.val
        helper(root)
        return self.ans
    
        