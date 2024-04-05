class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0 
        j = len(nums)-1
        while i < j:
            m = (j-i)//2 + i
            if nums[m] < nums[j]:
                j = m
            elif nums[m] > nums[j]:
                i = m + 1
            else:
                break   # for duplicate val
        return nums[i]
