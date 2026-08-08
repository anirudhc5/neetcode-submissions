class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [1 for i in range(size)]
        product_left = 1
        product_right = 1
        for i in range(size):
            ans[i] = product_left
            product_left *= nums[i]
        for j in range(size-1, -1, -1):
            ans[j] *= product_right
            product_right *= nums[j]
        # print(products_left, products_right)

        return ans
        