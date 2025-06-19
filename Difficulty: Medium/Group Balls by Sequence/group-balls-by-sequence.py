from collections import defaultdict

class Solution:
    def validgroup(self, arr ,k):
        n = len(arr)
        map = defaultdict(int)
        for val in arr:
            map[val] += 1
        for val in sorted(map.keys()):
            freq = map.get(val, 0)
            if freq == 0:
                continue
            for i in range(1, k):
                v = val + i
                f = map.get(v, 0)
                if f < freq:
                    return False
                map[v] -= freq
        return True
        # Code here