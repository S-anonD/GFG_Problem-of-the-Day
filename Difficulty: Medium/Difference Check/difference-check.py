class Solution:
    def minDifference(self, arr):
        totalSec = 24 * 3600
        seen = [False] * totalSec
        n = len(arr)
        for i in range(n):
            sec = self.toSeconds(arr[i])
            if seen[sec]:
                return 0
            seen[sec] = True
        first = -1
        last = -1
        prev = -1
        minDiff = float('inf')
        for i in range(totalSec):
            if not seen[i]:
                continue
            if prev != -1:
                minDiff = min(minDiff, i - prev)
            else:
                first = i
            prev = i
            last = i
        wrap = first + totalSec - last
        minDiff = min(minDiff, wrap)
        return minDiff
        # code here
    
    def toSeconds(self, time):
        h = int(time[0:2])
        m = int(time[3:5])
        s = int(time[6:8])
        return h * 3600 + m * 60 + s
