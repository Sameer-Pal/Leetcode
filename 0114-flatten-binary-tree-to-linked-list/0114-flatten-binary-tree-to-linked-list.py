# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
     if root == None:
        return 
     curr = root
     while curr:
        if curr.left:
            temp = curr.left
            while temp.right:
                temp = temp.right
            temp.right = curr.right
            curr.right = curr.left #  curr.leftt ko shift kro cur.right
            curr.left = None        # left mae har jaagh null krdo
        curr = curr.right


