#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        s, e = 0, 0
        res = []
        curr = 0
        for i in range(len(arr)):
            curr += arr[i]
            if curr >= target:
                e = i
                while curr > target and s < e:
                    curr -= arr[s]
                    s += 1
                if curr == target:
                    res.append(s + 1)
                    res.append(e + 1)
                    return res
        return [-1]
        # code here


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends