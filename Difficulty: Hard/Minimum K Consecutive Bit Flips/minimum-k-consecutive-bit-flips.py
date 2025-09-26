class Solution:
    def kBitFlips(self, arr, k):
        cur_window_flips = 0
        res = 0
        for i in range(len(arr)):
            if i - k >= 0 and arr[i - k] == 2:
                cur_window_flips -= 1
            if (cur_window_flips + arr[i]) % 2 == 0:
                if i + k > len(arr):
                    return -1
                arr[i] = 2
                cur_window_flips += 1
                res += 1
        return res
        # code here
        