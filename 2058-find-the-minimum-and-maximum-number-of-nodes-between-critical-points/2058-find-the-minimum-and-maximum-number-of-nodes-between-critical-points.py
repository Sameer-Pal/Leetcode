# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
      if not head or not head.next or not head.next.next:
            return [-1,-1]
      cp=[-1,-1]
      aux=[]
      prev=head
      curr=head.next
      nxt=curr.next
      ln=2
      while nxt:
          if prev.val < curr.val and nxt.val < curr.val:
              aux.append(ln) 
          if prev.val > curr.val and nxt.val > curr.val:
              aux.append(ln)
          ln+=1
          prev=prev.next
          curr=prev.next
          nxt=curr.next
    #   aux.sort()
    #   maxx=1
    #   minn=10**5
    #   for i in range(len(aux)):
    #       for j in range(i+1,len(aux)):
    #        diff = aux[j] - aux[i]
    #        minn=min(minn,diff)
    #        maxx=max(maxx,diff)
    #   cp=[minn,maxx]
    #   if cp!=[10**5,1]:
    #       return cp
    #   else: return [-1,-1]
      minn= 10**5
      
      if len(aux)<2:
          return [-1,-1]
      else:
          for i in range(1,len(aux)):
              minn=min(minn, aux[i] - aux[i-1])
      return [minn, aux[-1] - aux[0]]
