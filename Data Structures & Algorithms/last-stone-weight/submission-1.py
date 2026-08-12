import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush_max(heap, stone)

        while len(heap) >= 2:
            # print(heap)
            s1 = heapq.heappop_max(heap)
            s2 = heapq.heappop_max(heap)

            if s1 > s2:
                heapq.heappush_max(heap, (s1-s2))
            elif s1 < s2:
                heapq.heappush_max(heap, (s2-s1))
        
        return 0 if not heap else heap[0]