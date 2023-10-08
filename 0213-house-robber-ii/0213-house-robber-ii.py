class Solution:
    def rob(self, arr: List[int]) -> int:
        def help(arr):
            prev2=0
            prev1=arr[0]
            for i in range(1,len(arr)):
                pick=arr[i]+prev2 
                not_pick=prev1
                curr=max(pick,not_pick)
                prev2=prev1 
                prev1 =curr
            return prev1 
        if len(arr)==1: return arr[0]
        arr1=[]
        arr2=[]
        for i in range(len(arr)):
            if i!=0: arr1.append(arr[i])
            if i!=len(arr)-1: arr2.append(arr[i])
        return max(help(arr1),help(arr2))


        