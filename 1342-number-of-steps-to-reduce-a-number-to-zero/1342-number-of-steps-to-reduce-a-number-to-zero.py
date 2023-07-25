class Solution:
    def numberOfSteps(self, n: int) -> int:
        return self.helper(n,0)
    #    if n==0: return 0
    #    if n%2==0: return 1 + self.numberOfSteps(n//2)
    #    if n%2 == 1: return 1 +  self.numberOfSteps(n-1)
        
    def helper(self,n,steps):
         if n==0: return steps
         if n%2==0: return self.helper(n//2,steps+1)
         return self.helper(n-1,steps+1)
        
