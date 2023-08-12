#User function Template for python3

class Solution:
    def checkDoorStatus(self, N):
        res=[0]*(N+1)
        for i in range(1,N+1):
            for j in range(i,N+1,i):
                res[j]^=1
        return res[1:]
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        ptr = ob.checkDoorStatus(N)
        print(*ptr)
# } Driver Code Ends