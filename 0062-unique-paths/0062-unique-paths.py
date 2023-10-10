class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      prev=[0]*n 
      for i in range(m):
          curr=[0]*n
          for j in range(n):
              if i==0 or j ==0: curr[j]=1
              else:
                  up=0
                  left=0
                  if i>0:
                      up=prev[j]
                  if j>0: 
                      left=curr[j-1] 
                  curr[j]=left+up
          prev=curr 
      return prev[n-1]  