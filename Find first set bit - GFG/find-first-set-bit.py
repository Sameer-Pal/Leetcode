#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
     if n==0: return 0
     strr=""
     while n>0:
        bits=str(n%2)
        strr=bits+strr
        # print(strr)
        n=n//2
     for i in range(len(strr)-1,-1,-1):
       if strr[i] == "1": 
           return len(strr)-i
            
        
                

#{ 
 # Driver Code Starts.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        
        print(ob.getFirstSetBit(n))
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
# } Driver Code Ends