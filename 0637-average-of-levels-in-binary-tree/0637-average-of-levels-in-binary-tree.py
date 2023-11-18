# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res=[]
        if not root: return res
        qu=deque()   #curr_lvl_of_tree
        qu.append(root)  
        while qu:
            size=len(qu)
            curr_sum = 0
            for _ in range(size):
                curr_node = qu.popleft()
                curr_sum+=curr_node.val
                if curr_node.right:
                    qu.append(curr_node.right)
                if curr_node.left:
                    qu.append(curr_node.left)
            res.append(curr_sum / size)
        return res