import math
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # goal: find the value where the one before it is greater.
        # what i can do: check at the center every time to see if the current one is greater than the last one. if so, move l to the right, otherwise move r to the left.
        if nums[0] < nums[-1]: return nums[0] 
        l, r = 0, len(nums) - 1
        while l <= r and l >= 0 and r <= len(nums) - 1:
            # print(l, r)
            c = (l+r) // 2
            if nums[c] <= nums[-1]:
                if nums[c-1] > nums[c]: return nums[c]
                else: r = c-1
            else:
                l = c + 1
        return nums[0]