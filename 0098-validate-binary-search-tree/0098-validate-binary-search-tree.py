# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, low, high):
            if  node ==  None:
             return True
            if node.val <= low or node.val >= high:
                return False
            
            left_tree = helper(node.left, low, node.val)
            right_tree = helper(node.right, node.val, high)
            return left_tree and right_tree
        return helper(root,float("-inf"), float("inf"))


        