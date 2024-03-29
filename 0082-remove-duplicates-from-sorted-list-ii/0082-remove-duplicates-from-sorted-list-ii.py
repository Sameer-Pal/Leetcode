# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr=head
        dummy=ListNode(0)
        dummy.next = head
        curr= dummy
        while curr:
            if curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                temp = curr.next.next
                while temp and temp.next and temp.val == temp.next.val:
                    temp=temp.next
                curr.next = temp.next               
            else:
              curr=curr.next
        return dummy.next
