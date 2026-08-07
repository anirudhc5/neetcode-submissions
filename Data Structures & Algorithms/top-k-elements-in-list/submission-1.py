import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        cts = {}

        for num in nums:
            if num in cts: cts[num] += 1
            else: cts[num] = 1

        for num in cts:
            curr_count = cts[num]
            if len(heap) < k:
                heapq.heappush(heap, (curr_count, num))
            else:

                if heap[0][0] < curr_count:
                    heapq.heapreplace(heap, (curr_count, num))
        ans = []
        for freq, num in heap:
            ans.append(num)
        return ans