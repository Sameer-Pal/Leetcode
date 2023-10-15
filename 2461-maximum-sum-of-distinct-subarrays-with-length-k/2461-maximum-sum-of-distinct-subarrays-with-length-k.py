class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxsum = 0
        i = 0
        j = 0
        m = dict()
        s = 0  
        while j < n:
            s += nums[j]
            if nums[j] not in m:
                m[nums[j]] = 1
            else:
                m[nums[j]] += 1
            if j - i + 1 == k:
                if len(m) == k: 
                    maxsum = max(maxsum, s)
                s -= nums[i]
                m[nums[i]] -= 1
                if m[nums[i]] == 0:
                    m.pop(nums[i])
                i += 1
            j += 1
        return maxsum