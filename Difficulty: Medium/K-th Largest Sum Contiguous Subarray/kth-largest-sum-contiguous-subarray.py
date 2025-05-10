from typing import List


class Solution:
    def kthLargest(self, arr, k) -> int:
        n = len(arr)
        sum = [0] * (n + 1)
        sum[0] = 0
        sum[1] = arr[0]
        for i in range(2, n + 1):
            sum[i] = sum[i - 1] + arr[i - 1]
        pq = []
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                x = sum[j] - sum[i - 1]
                if len(pq) < k:
                    heapq.heappush(pq, x)
                else:
                    if pq[0] < x:
                        heapq.heapreplace(pq, x)
        return pq[0]
        # code here
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

# Position this line where user code will be pasted.

#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.kthLargest(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends