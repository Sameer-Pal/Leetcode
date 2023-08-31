class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(start, current_subset):
  
            if start == len(nums):
                result.append(current_subset[:])
                return
            
            # Include the current number in the subset
            current_subset.append(nums[start])
            helper(start + 1, current_subset)
            
            # Exclude the current number from the subset
            current_subset.pop()
            helper(start + 1, current_subset)
        
        result = []
        helper(0, [])
        return result
