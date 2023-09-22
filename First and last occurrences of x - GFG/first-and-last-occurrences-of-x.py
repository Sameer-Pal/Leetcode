#User function Template for python3


class Solution:
    def find(self, arr, n, x):
  
        first=self.binary_search(arr,x,True)
        last=self.binary_search(arr,x,False)
        ans=[-1,-1]
        ans[0]=first
        ans[1]=last
        return ans
    def binary_search(self,arr,x,Firstindex):
        i=0
        j=len(arr)-1
        
        ans=-1
        while i <=j:
            m=i+(j-i)//2
            if arr[m]<x:
                i=m+1
                
            elif arr[m]>x:
                j=m-1
            else:
                ans=m
                if Firstindex:
                    j=m-1
                else:
                    i=m+1

        return ans
                    
                    
                
                
                


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends