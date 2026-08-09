import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat_bananas(arr, k):
            time = 0
            for i in range(len(arr)):
                time += arr[i]//k + (arr[i]%k > 0)
            return time
        
        l, r = 1, max(piles)
        ans = float(math.inf)
        while l <= r:
            k = (l+r) // 2
            result = eat_bananas(piles, k)
            # print(k, result)
            if result > h:
                l = k + 1
            else:
                if k < ans: ans = k
                r = k - 1
        return ans