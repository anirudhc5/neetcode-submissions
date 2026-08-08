class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [1 for i in range(size)]
        product_left = 1
        product_right = 1
        i = 0
        j = size - 1
        while i < size:
            ans[i] *= product_left
            ans[j] *= product_right
            product_left *= nums[i]
            product_right *= nums[j]
            i+=1
            j-=1
        # print(products_left, products_right)

        return ans
        