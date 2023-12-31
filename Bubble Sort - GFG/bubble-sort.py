#User function Template for python3

class Solution:
    # Function to sort the array using bubble sort algorithm.
    def bubbleSort(self, arr, n):
        for i in range(n):
            # Last i elements are already sorted, so we don't need to check them again.
            for j in range(0, n-i-1):
                # Swap if the element found is greater than the next element.
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
        print()

# } Driver Code Ends