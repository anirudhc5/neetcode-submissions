class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return ""
        lens = []
        for s in strs:
            lens.append(str(len(s))+",")
        ans = "".join(lens)[:-1] + "#" + "".join(strs)
        # print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        if s == "": return []
        idx = s.find("#")
        sizes = s[:idx].split(",")
        words = s[idx+1:]
        # print(sizes, words)
        ans = []
        ptr = 0
        for size in sizes:
            currsize = int(size)
            if size == 0: ans.append("")
            ans.append(words[ptr:ptr+currsize])
            ptr+=currsize
        return ans
