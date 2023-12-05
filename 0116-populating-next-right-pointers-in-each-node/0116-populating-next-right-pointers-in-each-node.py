"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
 def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    # Without using queue
    if root == None:
        return None
    leftmost=root

    while leftmost.left:
        curr=leftmost
        while curr:   #  curr level 
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr=curr.next
        # curr level is over
        leftmost=leftmost.left
    return root

