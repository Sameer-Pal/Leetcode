#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        max_len=0
        summ=0
        mapp={}
        for i in range(n):
            summ+=arr[i]
            if summ==k:
                max_len=max(max_len,i+1)
            rem=summ-k
            if rem in mapp:
                l=i-mapp[rem]
                max_len=max(max_len,l)
            if summ not in mapp:
                mapp[summ]=i
        return max_len
#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends