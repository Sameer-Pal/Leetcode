# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        if N==1:
            return 1
        summ_front=0
        summ_rear=sum(A)
        for i in range(len(A)):
           summ_rear-=A[i]
           if summ_front==summ_rear:
                return i + 1
           summ_front+=A[i]
        return -1
#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends