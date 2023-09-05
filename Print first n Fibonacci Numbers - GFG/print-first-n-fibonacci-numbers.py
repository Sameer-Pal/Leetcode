#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
      a=1
      b=1
      fib_list=[]
      for  i in range(n):
          fib_list.append(a)
          a,b=b,a+b
      return fib_list
         
      
      

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends