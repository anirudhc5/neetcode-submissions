class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starts = set()
        nums = {*nums}
        ans = 0
        for num in nums:
            if num-1 not in nums: 
                starts.add(num)
                curr = num + 1
                length = 1
                while curr in nums:
                    length += 1
                    curr += 1
                if length > ans: ans = length
        return ans
        

            