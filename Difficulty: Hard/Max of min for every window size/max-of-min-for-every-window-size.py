class Solution:
    def maxOfMins(self, arr):
        n = len(arr)
        res = [0] * n
        windowMax = [0] * (n + 1)
        st = []
        for i in range(n):
            while st and arr[st[-1]] >= arr[i]:
                top = st.pop()
                left = st[-1] if st else -1
                right = i
                wsize = right - left - 1
                windowMax[wsize] = max(windowMax[wsize], arr[top])
            st.append(i)
        while st:
            top = st.pop()
            left = st[-1] if st else -1
            right = n
            wsize = right - left - 1
            windowMax[wsize] = max(windowMax[wsize], arr[top])
        for i in range(n):
            res[i] = windowMax[i + 1]
        for i in range(n - 2, -1, -1):
            res[i] = max(res[i], res[i + 1])
        return res
       # code here