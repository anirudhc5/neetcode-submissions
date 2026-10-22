from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = defaultdict(int)
        start = 0
        ans = 0
        i = 0
        while i < len(s):
            ch = s[i]
            if ch not in hmap:
                hmap[ch] = i
            else:
                original = hmap[ch]
                length = i - start
                if length > ans: ans = length
                start = max(original + 1, start)
                hmap[ch] = i
            i += 1
        if i - start > ans: ans = i - start
        return ans
            
        