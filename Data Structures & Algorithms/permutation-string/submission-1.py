class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, j = 0, len(s1) - 1
        s1map = {}
        for ch in s1:
            if ch not in s1map: s1map[ch] = 1
            else: s1map[ch] += 1
        while j < len(s2):
            s2map = {}
            for ch in s2[i:j+1]:
                if ch not in s2map: s2map[ch] = 1
                else: s2map[ch] += 1
            if s1map == s2map: return True
            i+=1
            j+=1
        return False
        