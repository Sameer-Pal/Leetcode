# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        # lst=deque()
        def helper(node):   #preorder traversal
            if not node:
                return "null,"# recrsn. stack out
            serialized = str(node.val) + ","
            
            # lst.append(str(node.val))
            serialized+=helper(node.left)
            serialized+=helper(node.right)
            return serialized
        # helper(root)
        return helper(root)
    def deserialize(self, data):
        def helper2(lst):
          curr=lst.pop(0)
          if curr == "null":
              return None
          node = TreeNode(int(curr))
          node.left = helper2(lst)
          node.right = helper2(lst)
          return node
        lst = data.split(",")
        return helper2(lst)

        

