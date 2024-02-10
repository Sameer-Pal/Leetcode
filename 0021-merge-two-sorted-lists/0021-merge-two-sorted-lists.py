class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr1=list1
        curr2=list2
        temp = dummy
        while curr1 and curr2:
            if curr1.val < curr2.val:
                temp.next = curr1
                curr1=curr1.next
            else:
                temp.next = curr2
                curr2 = curr2.next 
            temp = temp.next
        if curr1:
            temp.next = curr1 
        if curr2:
            temp.next = curr2
        return dummy.next 