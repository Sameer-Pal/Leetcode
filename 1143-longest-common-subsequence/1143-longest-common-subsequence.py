class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        def help(i,j):
            if i>=len(text1) or j>=len(text2):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]

            if text1[i]== text2[j]:
                dp[i][j] = 1+ help(i+1,j+1)
                
            else:
                dp[i][j] = max(help(i+1,j),help(i,j+1))
            return dp[i][j]
        return help(0,0)
        #  O(n*m)-t(c)
        # O(n*m) + O(n+m)(stack space) -S(c)
         
