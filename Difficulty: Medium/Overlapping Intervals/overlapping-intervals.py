class Solution:
	def mergeOverlap(self, arr):
	    arr.sort()
	    res = []
	    res.append(arr[0])
	    
	    for i in range(1, len(arr)):
	        last = res[-1]
	        curr = arr[i]
	        
	        if curr[0] <= last[1]:
	            last[1] = max(last[1], curr[1])
	        else:
	            res.append(curr)
	    return res
		#Code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        obj = Solution()
        ans = obj.mergeOverlap(arr)
        for i in ans:
            for j in i:
                print(j, end=" ")
        print()

# } Driver Code Ends