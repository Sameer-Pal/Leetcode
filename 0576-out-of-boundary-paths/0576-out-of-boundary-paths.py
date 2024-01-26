class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp={}
        def helper(i, j, N):
            if i == m or j == n or i < 0 or j < 0:
                return 1  
            if N == 0:
                return 0 
            key = (i, j, N)
            if key in dp:
                return dp[key]
            
            
            result = (helper(i - 1, j, N - 1) +
                      helper(i + 1, j, N - 1) +
                      helper(i, j - 1, N - 1) +
                      helper(i, j + 1, N - 1)) % (10**9 + 7)

            dp[key] = result
            return result

        return helper(i, j, N)