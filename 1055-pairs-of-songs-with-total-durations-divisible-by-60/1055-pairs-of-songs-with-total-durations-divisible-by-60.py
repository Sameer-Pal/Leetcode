class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count_pairs={}
        count=0
        for i in time:
            rem = i % 60
            remain_rem = (60-rem) % 60
            if remain_rem in count_pairs:
                count+=count_pairs[remain_rem]
            if rem not in count_pairs:
                count_pairs[rem] = 1
            else:
                count_pairs[rem] += 1
        return count    