#User function Template for python3

class Solution:
    def isLucky(self, n):
        return self.help(n,2)
    def help(self,n,counter):
            
            if n%counter==0:
                return 0
            elif counter>n:
                return 1
            return self.help(n-n//counter,counter+1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        obj = Solution()
        if obj.isLucky(n):
            print(1)
        else:
            print(0)
        
# } Driver Code Ends