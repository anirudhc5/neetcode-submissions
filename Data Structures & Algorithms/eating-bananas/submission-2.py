import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        ans = float(math.inf)
        while l <= r:
            k = (l+r) // 2
            result = 0
            for i in range(len(piles)):
                result += piles[i]//k + (piles[i]%k > 0)
            # print(k, result)
            if result > h:
                l = k + 1
            else:
                if k < ans: ans = k
                r = k - 1
        return ans