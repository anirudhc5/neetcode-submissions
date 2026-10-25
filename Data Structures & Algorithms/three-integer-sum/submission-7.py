class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        seen = set()
        for i in range(len(nums) - 2):
            j = i+1
            k = len(nums) - 1
            rem = -nums[i]
            while j < k:
                if nums[j]+nums[k]==rem:
                    new = [-rem, nums[j], nums[k]]
                    tup = (-rem, nums[j], nums[k])
                    if tup not in seen:
                        ans.append([-rem, nums[j], nums[k]])
                        seen.add((-rem, nums[j], nums[k]))
                    j+=1
                    k-=1
                elif nums[j]+nums[k] < rem:
                    j+=1
                elif nums[j]+nums[k] > rem:
                    k-=1
        return ans
