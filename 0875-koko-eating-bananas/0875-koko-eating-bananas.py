class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start= 1
        end = max(piles)
        res = end
        while start <= end:
            m = start + (end-start)//2
            hours = 0 
            for i in piles:
                hours += math.ceil(i/m)
            if hours <= h:
                res = min(res,m)
                end = m - 1 #elinating the right side 
            else:
                start = m + 1  #eliminating the left side
        return res
        