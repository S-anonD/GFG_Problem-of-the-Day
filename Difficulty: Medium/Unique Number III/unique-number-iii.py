#User function Template for python3

class Solution:
    def getSingle(self, arr):
        ones, twos = 0, 0
        for num in arr:
            twos |= ones & num
            ones ^= num
            mask = ~(ones & twos)
            ones &= mask
            twos &= mask
        return ones
        # code here 


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSingle(arr)
        print(ans)
        print("~")
# } Driver Code Ends