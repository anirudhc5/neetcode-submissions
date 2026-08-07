class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        ans = 0

        while i < j:
            # print(f"{heights[i]} ({i}) x {heights[j]} ({j})")
            diff = j-i
            if heights[i] < heights[j]:
                area = heights[i] * diff
                if area > ans: ans = area
                i+=1
            else:
                area = heights[j] * diff
                if area > ans: ans = area
                j-=1

        return ans