#User function Template for python3

class Solution:
    def countWays(self,n):
      count = [0] * (n + 1)

      count[0] = 1
      if n >= 1 :
        count[1] = 1
      if n >= 2 :
        count[2] = 2

      for i in range(3, n + 1):
        count[i] = (count[i-1] +
                   count[i-2] + count[i-3])
         
      return count[n] % 1000000007;
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
# } Driver Code Ends