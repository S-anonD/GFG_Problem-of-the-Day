# 14/11/24
# Nearly Sorted

from heapq import heappop, heappush, heapify
class Solution:
    def nearlySorted(self, arr, k):
        heap = arr[:k + 1]
        heapify(heap)
        target_index = 0
        
        for rem_elmnts_index in range(k + 1, len(arr)):
            arr[target_index] = heappop(heap)
            heappush(heap, arr[rem_elmnts_index])
            target_index += 1
        
        while heap:
            arr[target_index] = heappop(heap)
            target_index += 1
        return