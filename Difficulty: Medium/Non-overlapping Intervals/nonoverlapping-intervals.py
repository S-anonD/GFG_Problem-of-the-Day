#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minRemoval(self, intervals):
        cnt = 0
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                cnt += 1
            else:
                end = intervals[i][1]
        return cnt
        # Code here

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.minRemoval(intervals)
        print(res)
        print("~")
# } Driver Code Ends