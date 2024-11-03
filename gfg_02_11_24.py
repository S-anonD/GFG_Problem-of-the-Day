# 02/11/24
# Kth Distance

class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        mp = dict()
        for i in range(len(arr)):
            if arr[i] in mp:
                if (i - mp[arr[i]] <= k):
                    return True
                else:
                    mp[arr[i]] = i
            mp[arr[i]] = i
        return False