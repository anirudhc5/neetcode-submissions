from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cts = defaultdict(int)
        i = 0
        ans = 0
        mostfreq = 0
        for j in range(len(s)):
            ch = s[j]
            cts[ch] += 1
            if cts[ch] > mostfreq: mostfreq = cts[ch]
            if (j-i+1) - mostfreq > k:
                cts[s[i]] -= 1
                i += 1
        if j-i+1 > ans: ans = j-i+1
        return ans

        