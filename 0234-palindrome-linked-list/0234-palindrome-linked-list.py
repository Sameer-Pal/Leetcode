# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        def rev(node):
            prev=None
            curr=node
            while curr:
                nextnode=curr.next
                curr.next=prev
                prev=curr
                curr=nextnode
            return prev
        slow=head
        fast=head
        while fast.next and fast.next.next:   # kyoki next bhi null hua tobhi aage nahi bhadna 
            slow=slow.next
            fast=fast.next.next
        newhead= rev(slow.next)
        first=head
        second=newhead
        while second:
            if first.val!= second.val:
                return False
            first = first.next
            second = second.next
        return True
