class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rev(s):
            return s[::-1]
        def invert(s):
          res=""
          for i in s:
           if i == "1":
            res+="0"
           elif i == "0":
            res+="1"
          return res 
        def helper(n):
            if n == 1:
                return "0"
            prev = helper(n - 1)
            return prev + "1" + rev(invert(prev))        
        s_n=helper(n)
        return s_n[k-1]