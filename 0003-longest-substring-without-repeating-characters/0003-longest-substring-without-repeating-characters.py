class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s) 
        if n==0: return 0
        max_length = 0
        char_set = deque()
        
        i,j=0,0
        while  i<n:
             if s[i] not in char_set:
                 char_set.append(s[i])
                 
                 max_length=max(max_length,i-j+1)
                 i+=1
             else:
                 char_set.remove(s[j])
                 j+=1
        return max_length
       