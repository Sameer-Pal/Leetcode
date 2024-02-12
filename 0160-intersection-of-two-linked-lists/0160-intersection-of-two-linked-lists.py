# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def length(node):
            curr= node
            lent=0 
            while curr:
                lent+=1
                curr=curr.next
            return lent

        lena=length(headA)
        lenb=length(headB)
        curra= headA
        currb= headB

        while lena>lenb:
            lena-=1
            curra = curra.next
        while lenb > lena:
            lenb-=1
            currb=currb.next
        while curra!= currb:
            curra=curra.next
            currb=currb.next
        return curra