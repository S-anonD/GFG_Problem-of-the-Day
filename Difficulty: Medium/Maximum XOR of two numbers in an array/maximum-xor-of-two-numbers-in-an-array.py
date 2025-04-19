#User function Template for python3

class Solution:
    def maxXor(self, arr):
        res, mask = 0, 0
        s = set()
        for i in range(30, -1, -1):
            mask |= (1 << i)
            for num in arr:
                s.add(num & mask)
            curr = res | (1 << i)
            for prefix in s:
                if curr ^ prefix in s:
                    res = curr
                    break
            s.clear()
        return res
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxXor(arr))
        print("~")

# } Driver Code Ends