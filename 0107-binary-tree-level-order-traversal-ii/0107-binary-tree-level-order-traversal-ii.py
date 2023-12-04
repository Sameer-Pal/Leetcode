# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if root is None:
            return res
        q = deque()
        q.append(root)
        while q:
            curr_size = len(q)
            curr_lvl = []
            for i in range(curr_size):
                        curr_node=q.popleft()
                        curr_lvl.append(curr_node.val)
                        if curr_node.left:
                            q.append(curr_node.left)
                        if curr_node.right:
                            q.append(curr_node.right)
            res.insert(0,curr_lvl)
        # new=[]
        # new=res[::-1]
        return res
                        
