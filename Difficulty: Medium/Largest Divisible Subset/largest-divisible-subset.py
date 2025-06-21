class Solution:
    def largestSubset(self, arr):
        arr.sort(reverse=True)
        n = len(arr)
        dp = [1] * n
        parent = [-1] * n
        max_size = 1
        last_index = 0
        for i in range(1, n):
            for j in range(i):
                if arr[j] % arr[i] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if dp[i] > max_size:
                max_size = dp[i]
                last_index = i
        res = []
        while last_index >= 0:
            res.append(arr[last_index])
            last_index = parent[last_index]
        return res
        #code here