import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        hmap = defaultdict(int)
        for num in nums:
            hmap[num] += 1
        for key in hmap:
            if len(heap) < k:
                heapq.heappush(heap, (hmap[key], key))
            else:
                count = heap[0][0]
                if hmap[key] > count:
                    heapq.heapreplace(heap, (hmap[key], key))
        ans = []
        for tup in heap:
            ans.append(tup[1])
        return ans