class Solution:
    def assignHole(self, mices, holes):
        mices.sort()
        holes.sort()
        n = len(mices)
        Max = 0 
        for i in range(n):
            if (Max < abs(mices[i] - holes[i])):
                Max = abs(mices[i] - holes[i])
        return Max
        # code here
        