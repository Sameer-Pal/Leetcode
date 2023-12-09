class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia=0
        def lev(node):
            nonlocal dia
            if node == None:
                return 0
            l =  lev(node.left)
            r = lev(node.right)
            d =  r + l 
            dia = max(dia,d)
            return max(l,r) + 1
        lev(root)
        return dia
