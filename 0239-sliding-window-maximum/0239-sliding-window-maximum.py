class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queu, res = deque(), [] 
        for r in range(len(nums)):

            while queu and nums[queu[-1]] < nums[r]:
                queu.pop()
            queu.append(r)
            if r+1 < k: continue
            if queu[0] < r-k+1:
                queu.popleft()
            res.append(nums[queu[0]])

        return res