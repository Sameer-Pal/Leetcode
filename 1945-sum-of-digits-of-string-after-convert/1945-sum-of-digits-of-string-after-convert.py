class Solution:
    def getLucky(self, s: str, k: int) -> int:
        c=""
        for i in s:
            c+=str(ord(i)-96)
        print(c)
        for _ in range(k):
            sm=0
            for j in c:
                sm+=int(j)
            c=str(sm)
            # print(c)
        return int(c)  
