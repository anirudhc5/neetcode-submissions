class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        vals = {}
        for idx, num in enumerate(nums):
            if num in vals: vals[num].append(idx)
            else: vals[num] = [idx]
        ans = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                twosum = nums[i] + nums[j]
                if -twosum in vals:
                    potential_ans = [nums[i],nums[j],-twosum]
                    if potential_ans in ans: continue
                    for thirdidx in vals[-twosum]:
                        if thirdidx <= j: continue
                        ans.append(potential_ans)
                        break
        return ans
