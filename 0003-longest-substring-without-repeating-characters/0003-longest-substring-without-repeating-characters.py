class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s) 
        if n==0: return 0
        max_length = 0
        char_set = deque()
        for i in s:
             while i in char_set: 
               char_set.popleft()
             char_set.append(i)
             max_length=max(max_length,len(char_set))
         
  
        return max_length
       