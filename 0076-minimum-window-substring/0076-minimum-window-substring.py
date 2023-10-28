class Solution:
  def minWindow(self, s: str, t: str) -> str:
    if len(t) > len(s):
        return ""

    i, j = 0, 0
    minWindowSize = float("inf")
    start_i = 0
    mp = defaultdict(int)
    curr_window = 0
    req_count = len(t)

    for char in t:
        mp[char] += 1

    while j < len(s):
        if mp[s[j]] > 0:
            req_count -= 1
        mp[s[j]] -= 1

        while req_count == 0:
            if minWindowSize > (j - i + 1):
                start_i = i
                minWindowSize = j - i + 1

            mp[s[i]] += 1

            if mp[s[i]] > 0:
                req_count += 1

            i += 1

        j += 1

    if minWindowSize == float("inf"):
        return ""
    else:
        return s[start_i : start_i + minWindowSize]
             