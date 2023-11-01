class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        temp = pref[0]
        for i in range(1, len(pref)):
            temp, pref[i] = pref[i], pref[i]^temp
        return pref
