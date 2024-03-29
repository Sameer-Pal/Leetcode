class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        # if len(h)==1: return h[0]
        maxi = 0
        stk=[]
        for  i in range(len(h)):
            start = i
            while stk and stk[-1][1] > h[i]:
                idx, ht = stk.pop()
                maxi = max( ht* (i-idx), maxi)
                start = idx
            stk.append([start, h[i]])
        for i, ht in stk:
            maxi = max(maxi, (len(h)-i) * ht)
        return maxi
             