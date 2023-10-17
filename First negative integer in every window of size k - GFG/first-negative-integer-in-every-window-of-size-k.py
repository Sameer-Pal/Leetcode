

from collections import deque
def printFirstNegativeInteger( A, N, K):
    # code here
    i=0
    j=0
    ans=[]
    deq=deque()
    while j<N:
        if A[j]<0:
            deq.append(A[j])
        
        if j-i+1<K:
            j=j+1
            
        elif j-i+1==K:
            if len(deq)==0:
                ans.append(0)
            else:
                ans.append(deq[0])        
                
                #slide the window
                if A[i]==deq[0]:
                    deq.popleft()
            i=i+1
            j=j+1
    return(ans) 
#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends