# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
           return None
        if root == p or root == q:  # found oneof them ignore other node
            return root #ignoring other ele. as it's guarntedd its present in the tre
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left!= None and right!=None: # found item both in the l& right
            return root 
        return right if left is None else left  # for ancestor of itself