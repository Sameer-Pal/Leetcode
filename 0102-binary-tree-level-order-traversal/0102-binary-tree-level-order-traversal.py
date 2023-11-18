# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    result = []
    if not root:
        return result    
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_node = queue.popleft()    #remove every traversed node
            current_level.append(current_node.val)   #once traversed  add it in curr
 # for adding node.val in queue
            if current_node.left:
                queue.append(current_node.left) 
            if current_node.right:
                queue.append(current_node.right) 
        result.append(current_level)
    return result