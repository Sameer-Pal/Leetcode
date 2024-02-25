
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rev(node):    # reversing the fnctn.
            curr=node
            prev=None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev=curr
                curr=nxt
            return prev
        def kth_node(node,k):
            k-=1
            temp = curr
            while temp and k>0:
                k-=1
                temp = temp.next
            return temp
        curr=head
        prev=None
        while curr:
            kthnode=kth_node(curr,k)
            if kthnode==None:
                if prev:    # if kth node and there ie prev!=None then only connc tit with next 
                    prev.next = curr
                break
            nxt_node =  kthnode.next
            kthnode.next=None
            rev(curr)
            if curr == head:    
                head = kthnode
            else:
                prev.next=kthnode
            prev=curr
            curr=nxt_node
        return head