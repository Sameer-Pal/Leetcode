class Solution:
    def minPathSum(self, arr: List[List[int]]) -> int:
        m=len(arr)
        n=len(arr[0])
        dp=[[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
              if i==0 and  j==0: dp[i][j] = arr[0][0]
              else:
                    up=arr[i][j]
                    if i>0: up+=dp[i-1][j]
                    else: up+=float("inf")

                    left=arr[i][j]
                    if j>0:left+=dp[i][j-1]
                    else: left+=float("inf")
                    dp[i][j] = min(up,left)
        return dp[m-1][n-1]

        