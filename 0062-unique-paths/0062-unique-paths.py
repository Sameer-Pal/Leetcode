class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*n for k in range(m)]

        def helper(row,col):
            # nonlocal c
            if row==0 or  col==0:
                return 1 
            if row < 0 or col < 0:
                return 0
            if dp[row][col]!=-1:
                return dp[row][col]
            up = helper(row-1,col)
            left = helper(row,col-1)
            dp[row][col] = up+left
            return dp[row][col]
        return helper(m-1,n-1)
