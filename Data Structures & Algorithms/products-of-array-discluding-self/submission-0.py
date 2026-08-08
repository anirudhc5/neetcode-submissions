class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        products_left = {}
        products_right = {}

        for idx in range(len(nums)):
            if idx==0: products_left[idx] = nums[idx]
            else: products_left[idx] = products_left[idx-1] * nums[idx]
        
        for idx in range(len(nums)-1, -1, -1):
            if idx==len(nums)-1: products_right[idx] = nums[idx]
            else: products_right[idx] = products_right[idx+1] * nums[idx]
        # print(products_left, products_right)
        for idx in range(len(nums)):
            if idx == 0:
                ans.append(products_right[idx+1])
            elif idx == len(nums) - 1:
                ans.append(products_left[idx-1])
            else:
                ans.append(products_left[idx-1] * products_right[idx+1])

        return ans
        