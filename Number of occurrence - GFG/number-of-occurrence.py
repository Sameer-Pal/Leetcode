#User function Template for python3
class Solution:

    def count(self, arr, n, x):
        # Function to find the index of the first occurrence of x in arr
        def first_occurrence(arr, x):
            left, right = 0, n - 1

            while left <= right:
                mid = left + (right - left) // 2

                if arr[mid] == x:
                    if mid == 0 or arr[mid - 1] != x:
                        return mid
                    else:
                        right = mid - 1
                elif arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        # Function to find the index of the last occurrence of x in arr
        def last_occurrence(arr, x):
            left, right = 0, n - 1

            while left <= right:
                mid = left + (right - left) // 2

                if arr[mid] == x:
                    if mid == n - 1 or arr[mid + 1] != x:
                        return mid
                    else:
                        left = mid + 1
                elif arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        first_index = first_occurrence(arr, x)
        last_index = last_occurrence(arr, x)

        if first_index == -1 or last_index == -1:
            return 0

        return last_index - first_index + 1

# Example usage:


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends