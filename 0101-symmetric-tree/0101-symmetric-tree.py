 # # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      return root is None or self.help(root.left,root.right)
    def help(self, left, right): 
        if  left == None or   right == None:
            return left == right
        # if : return False
        return left.val == right.val and  self.help(left.left, right.right) and self.help(left.right, right.left)
