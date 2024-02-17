"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        tail = head
        stk=[]
        while curr:
            if curr.child:
                child = curr.child    # refrence to child 
                if curr.next:
                    stk.append(curr.next)
                    curr.next.prev = None    # curr-> agla  -> prev --> set to NONE
                curr.next = child         # child hold krne wali node ka child se connctn. uske prev ka bhi   
                child.prev = curr         
                curr.child = None           # child ko set krdo none    BCZ<it dissolved 
            tail = curr
            curr=curr.next 
        while stk:
            curr=stk.pop()
            curr.prev=tail
            tail.next = curr
            while  curr:
                tail=curr
                curr=curr.next 
        return head

