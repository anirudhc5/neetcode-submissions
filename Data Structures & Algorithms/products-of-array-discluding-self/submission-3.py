class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = []
        products_left = {-1:1}
        products_right = {size: 1}
        i = 0
        j = size - 1
        while i < size:
            products_left[i] = products_left[i-1] * nums[i]
            products_right[j] = products_right[j+1] * nums[j]
            i+=1
            j-=1
        for i in range(size):
            ans.append(products_left[i-1] * products_right[i+1])
        # print(products_left, products_right)

        return ans
        