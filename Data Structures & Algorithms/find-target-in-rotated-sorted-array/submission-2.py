class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        def find_min(nums):
            l, r = 0, len(nums) - 1
            if nums[l] < nums[r]: return 0
            while l <= r:
                c = (l+r)//2
                if c+1 >= len(nums): return 0
                if nums[c] > nums[c+1]: return c+1 # i found the point
                # what if my curr is greater than left? go right.
                # else? go left.
                if nums[c] > nums[l]:
                    l = c + 1
                else:
                    r = c - 1
            return 0


        # here's what i'll do:
        # i'll find the point where it first rotates. so left < right.
        # and when i do, i'm going to see if target is smaller than 0.
        # if so i'm going to look for the right half else look at the
        # left half.


        min_index = find_min(nums)
        l, r = 0, len(nums)

        # now that i've found the minimum index, i can compare the 0th index
        # and see if the target is greater. if greater? set r to min - 1.
        # otherwise? then just set l to min.

        if min_index != l:
            if target >= nums[0]: r = min_index - 1
            else: l = min_index

        while l <= r:
            c = (l+r)//2
            if c < 0 or c >= len(nums): return -1
            if nums[c] == target: return c
            elif target > nums[c]: l = c + 1
            else: r = c - 1

        return -1
        