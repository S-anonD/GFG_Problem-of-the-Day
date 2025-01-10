
class Solution:
    def countDistinct(self, arr, k):
        n = len(arr)  
        res = []
        freq = defaultdict(int)
        for i in range(k):
            freq[arr[i]] += 1
        res.append(len(freq))
        for i in range(k, n):
            freq[arr[i]] += 1
            freq[arr[i - k]] -= 1
            if freq[arr[i - k]] == 0:
                del freq[arr[i - k]]
            res.append(len(freq))
        return res
        # Code here


#{ 
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends