class Solution:
    def search(self, nums: List[int], target: int) -> int:
   
     peak =self.pivot(nums)
    
     if peak == -1:
         return self.bs(nums,target,0,len(nums)-1)
     elif target == nums[peak]:
         return peak
     elif target >= nums[0]:
         return self.bs(nums,target,0,peak-1)
     else:
         return self.bs(nums, target, peak+1, len(nums)-1)

    def bs(self,nums,target,start,end):
     while start <= end:
      m = start +(end-start)//2
      if target < nums[m]:
          end = m - 1
      elif target > nums[m]:
          start = m + 1
      else:
          return m
     return -1
    def pivot(self,nums):   
        start = 0
        end = len(nums)-1
      
        while start <= end:
            m=start + (end-start)//2
         
            if m < end and nums[m] > nums[m+1]:
                return m
          
            elif m>start and nums[m] < nums[m-1]:
                return m-1
           
            elif nums[start] <= nums[m]:
                start = m+1
          
            elif nums[start] >= nums[m]:
                end= m-1 
        return -1                   

         