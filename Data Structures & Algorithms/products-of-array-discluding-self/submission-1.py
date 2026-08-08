class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        size = len(nums)
        products_left = {-1:1}
        products_right = {size: 1}
        i = 0
        j = size - 1
        while i < size and j >= 0:
            products_left[i] = products_left[i-1] * nums[i]
            products_right[j] = products_right[j+1] * nums[j]
            i+=1
            j-=1
        # print(products_left, products_right)
        for idx in range(size):
            ans.append(products_left[idx-1] * products_right[idx+1])

        return ans
        