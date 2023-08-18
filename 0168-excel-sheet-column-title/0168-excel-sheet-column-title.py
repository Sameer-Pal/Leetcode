class Solution:
    def convertToTitle(self, num: int) -> str: 
        ans=""
        while num > 0:
            num -= 1
            ans = chr(num % 26 + 65) + ans
            num = num// 26
            # print(ans)
        return ans