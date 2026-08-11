class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        ans = 0
        freqs = {}
        mostfreq = 0
        for j in range(len(s)):
            if s[j] in freqs:
                freqs[s[j]] += 1
            else:
                freqs[s[j]] = 1
            if freqs[s[j]] > mostfreq: mostfreq = freqs[s[j]]
            
            if (j - i + 1) - mostfreq > k:
                freqs[s[i]] -= 1
                i += 1
        if j - i + 1 > ans: ans = j - i + 1
        return ans
            