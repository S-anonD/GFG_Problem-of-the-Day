import heapq
class Solution:
    def getMedian(self, arr):
        leftmaxheap = []
        rightminheap = []
        res = []
        for num in arr:
            heapq.heappush(leftmaxheap, -num)
            temp = -heapq.heappop(leftmaxheap)
            heapq.heappush(rightminheap, temp)
            if len(rightminheap) > len(leftmaxheap):
                temp = heapq.heappop(rightminheap)
                heapq.heappush(leftmaxheap, -temp)
            if len(leftmaxheap) != len(rightminheap):
                median = -leftmaxheap[0]
            else:
                median = (-leftmaxheap[0] + rightminheap[0]) / 2.0
            res.append(median)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.getMedian(nums)
        print(" ".join(f"{x:.1f}" for x in ans))


if __name__ == "__main__":
    main()

# } Driver Code Ends