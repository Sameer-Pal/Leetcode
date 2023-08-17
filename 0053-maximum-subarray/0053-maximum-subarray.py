class Solution:
    def maxSubArray(self, nums: List[int]) -> int:  

     
     s = 0
     maxi= nums[0]  
     for i in nums:
            s = s + i
            if s > maxi: maxi = s
            if s < 0: s = 0
     return maxi

     