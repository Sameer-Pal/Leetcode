class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def fn(node, k):
            count=1
            tail=node
            while tail:
                if count == k:
                    return tail
                tail=tail.next
                count+=1
            return tail

        if k == 0 or head is None:
            return head
        ln=1
        tail = head
        while  tail.next:
            ln+=1
            tail= tail.next
            
        if k % ln == 0:return head
        k = k % ln
        tail.next=head
        new_last = fn(head,ln-k)
        head=new_last.next
        new_last.next=None
        return head