class Solution:
	def pythagoreanTriplet(self, arr):
	    n = len(arr)
	    maxele = 0
	    for ele in arr:
	        maxele = max(maxele, ele)
        vis = [False] * (maxele + 1)
        for ele in arr:
            vis[ele] = True
        for a in range(1, maxele + 1):
            if not vis[a]:
                continue
            for b in range(1, maxele + 1):
                if not vis[b]:
                    continue
                c = int(math.sqrt(a * a + b * b))
                if (c * c) != (a * a + b * b) or c > maxele:
                    continue
                if vis[c]:
                    return True
        return False
    	# code here

import math