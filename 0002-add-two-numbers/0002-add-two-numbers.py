# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        summ=0
        dummy=ListNode(-1)
        curr=dummy
        c=0
        while l1 or l2 or c:
            summ=c
            if l1:
                summ += l1.val
                l1=l1.next 

            if l2:
                summ += l2.val   
                l2=l2.next   
            rem = summ % 10    
            c = summ // 10       
            curr.next = ListNode(rem)
            curr=curr.next 
        return dummy.next 

        
        
        
            
          