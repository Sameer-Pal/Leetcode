class Solution:
    def reverseString(self, s: List[str]) -> None:
        return self.help(s,len(s)-1)
        return s
    def help(self,s,i):
        

        if i < 0:
            return
        s.append(s.pop(i))
        self.help(s, i - 1)
        