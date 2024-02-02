class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        dig="123456789"
        ans=[]
        for i in range(len(dig)):
            for j in range(i+1, len(dig)+1):
                curr=int(dig[i:j])
                if low<= curr<= high:
                    ans.append(curr)
        ans.sort()
        return ans