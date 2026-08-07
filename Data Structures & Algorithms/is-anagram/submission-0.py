class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cts1 = {}
        cts2 = {}

        for ch in s:
            if ch not in cts1: cts1[ch] = 1
            else: cts1[ch] += 1

        for ch in t:
            if ch not in cts2: cts2[ch] = 1
            else: cts2[ch] += 1
        
        return cts1 == cts2
