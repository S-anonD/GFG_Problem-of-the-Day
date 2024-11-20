# 20/11/24
# Majority Element II

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        maj = []
        mp = dict()
        n = len(arr)
        for i in range(n):
            if arr[i] not in mp:
                if arr.count(arr[i]) > n/3:
                    maj.append(arr[i])
                mp[arr[i]] = arr.count(arr[i])
        return sorted(maj)