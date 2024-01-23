class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charset=set()
        def overlapp(charset,s):
            c=Counter(charset) + Counter(s)
            return max(c.values()) > 1
        

        def bktrk(i):
            if i == len(arr):   # at end of array
                return len(charset)
            res=0
            if not overlapp(charset, arr[i]):
                for c in arr[i]:
                    charset.add(c)
                res = bktrk(i+1)
                for c in arr[i]:
                    charset.remove(c)
            return max(res, bktrk(i+1))
        return bktrk(0)
