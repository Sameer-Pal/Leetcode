class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ss=0
        tt=0
        while ss<len(s) and tt<len(t):
            if s[ss]==t[tt]:
                ss+=1
            tt+=1
        return ss==len(s)