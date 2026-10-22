from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            buckets = [0] * 26
            for ch in s:
                buckets[ord(ch)-97] += 1
            groups[tuple(buckets)].append(s)
        return list(groups.values())
        