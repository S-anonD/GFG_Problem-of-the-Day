# User function Template for python3

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        n = len(arr)
        res = [-1] * n
        stk = []
        
        for i in range(n-1, -1, -1):
            while stk and arr[stk[-1]] <= arr[i]:
                stk.pop()
            if stk:
                res[i] = arr[stk[-1]]
            stk.append(i)
        return res
        # code here


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends