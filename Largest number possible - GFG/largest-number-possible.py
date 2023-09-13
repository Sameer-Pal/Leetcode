#User function Template for python3

class Solution:
    def findLargest(self, N, S):
        final=""
        digit=9
        if S==0 and N>1:
            return -1

        while N>0:
            if S>=digit:
                final+=str(digit)
                S-=digit
            else:
                final+=str(S)
                S=0
            N-=1
                
        if S!=0: return -1
        return int(final)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
# } Driver Code Ends