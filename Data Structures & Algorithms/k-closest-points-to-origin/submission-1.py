import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x, y = point[0], point[1]
            dist = (x**2 + y**2) ** 0.5
            if len(heap) < k:
                heapq.heappush_max(heap, (dist, x, y))
            elif dist < heap[0][0]:
                heapq.heapreplace_max(heap, (dist, x, y))
        ans = []
        for elem in heap:
            ans.append([elem[1], elem[2]])
        return ans