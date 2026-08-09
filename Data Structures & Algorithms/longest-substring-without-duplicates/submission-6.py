class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dct = {}
        ans = 0
        curr_length = 0
        for idx,ch in enumerate(s):
            # print(curr_length)
            if ch not in dct:
                # print("added")
                dct[ch] = idx
                curr_length +=1
            else:
                # print("repeat detected")
                if curr_length > ans: ans = curr_length
                if curr_length >= idx - (dct[ch]):
                    curr_length = idx - (dct[ch])
                else:
                    curr_length += 1
                dct[ch] = idx
        if curr_length > ans: ans = curr_length
        # print(curr_length)
        return ans
        