#User function Template for python3
class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        citations.sort(reverse=True)
        n = len(citations)
        i = 0
        while i < n and citations[i] > i:
            i += 1
        return i
        #code here


#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.hIndex(arr)

        print(result)
        print("~")

# } Driver Code Ends