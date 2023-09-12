class Solution:
    def isPerfectNumber(self, N):
        if N <= 1:
            return 0  

        factor_sum = 1 

        for i in range(2, int(N**0.5) + 1):
            if N % i == 0:
                factor_sum += i
                if i != N // i:
                    factor_sum += N // i

        if factor_sum == N: return 1
        else: return 0

          
          


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.isPerfectNumber(N))
# } Driver Code Ends