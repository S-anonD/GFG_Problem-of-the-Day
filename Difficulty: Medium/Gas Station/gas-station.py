class Solution:
    def startStation(self, gas, cost):
        n = len(gas)
        startidx = 0
        currgas = 0
        for i in range(n):
            currgas += (gas[i] - cost[i])
            if currgas < 0:
                startidx = i + 1
                currgas = 0
        currgas = 0
        for i in range(n):
            idx = (i + startidx) % n
            currgas += (gas[idx] - cost[idx])
            if currgas < 0:
                return -1
        return startidx
        # Your code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        gas = list(map(int, input().strip().split()))
        cost = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.startStation(gas, cost)
        print(ans)
        print("~")

# } Driver Code Ends