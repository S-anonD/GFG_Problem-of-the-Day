# 04/11/24
# Find All Triplets with Zero Sum

class Solution:
    def findTriplets(self, arr):
        # Your code here
        res = []
        mp = dict()
        n = len(arr)
        for i in range(n):
            if arr[i] not in mp:
                mp[arr[i]] = []
            mp[arr[i]].append(i)
        for i in range(n):
            for j in range(i+1, n):
                num = -(arr[i]+arr[j])
                if num in mp:
                    for k in mp[num]:
                        if k > j:
                            res.append([i, j, k])
        return res