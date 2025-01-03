class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        count = 0
        n = len(arr)
        temp_arr = [0]*n
        return self.tempSort(arr, temp_arr, 0, n - 1)
    
    def tempSort(self, arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right)//2
            inv_count += self.tempSort(arr, temp_arr, left, mid)
            inv_count += self.tempSort(arr, temp_arr, mid + 1, right) 
            inv_count += self.merge(arr, temp_arr, left, mid, right)
        return inv_count 
    
    def merge(self, arr, temp_arr, left, mid, right):
        i = left
        j = mid + 1
        k = left
        inv_count = 0
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                k += 1
                i += 1
            else:
                temp_arr[k] = arr[j] 
                inv_count += (mid-i + 1)
                k += 1
                j += 1
        while i <= mid:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        while j <= right:
            temp_arr[k] = arr[j]
            k += 1
            j += 1
        for loop_var in range(left, right + 1):
            arr[loop_var] = temp_arr[loop_var]
        return inv_count 
        # Your Code Here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends