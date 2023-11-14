# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left,right):
             if left > right:
                return None
             m =  (right + left)// 2  
             node = TreeNode(nums[m])
             node.left = helper(left,m-1)    # changng the val one-by-one when we see 
             node.right = helper(m+1,right)
             return node 
        return helper(0, len(nums)-1)
        
