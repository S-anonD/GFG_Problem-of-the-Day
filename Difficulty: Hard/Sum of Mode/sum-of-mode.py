class Solution:
    def sumOfModes(self, arr, k):
        n = len(arr)
        mp = defaultdict(int)
        st = []
        for i in range(k):
            mp[arr[i]] += 1
        for key, val in mp.items():
            heapq.heappush(st, (-val, key))
        def get_mode():
            while st and -st[0][0] != mp[st[0][1]]:
                heapq.heappop(st)
            return st[0][1]
        sum = get_mode()
        for i in range(k, n):
            out = arr[i - k]
            mp[out] -= 1
            in_ = arr[i]
            mp[in_] += 1
            heapq.heappush(st, (-mp[in_], in_))
            heapq.heappush(st, (-mp[out], out))
            sum += get_mode()
        return sum
        # code here
        
from collections import defaultdict
import heapq