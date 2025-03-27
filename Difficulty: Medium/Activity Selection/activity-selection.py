class Solution:
    def activitySelection(self, start, finish):
        ans = 0
        arr = []
        for i in range(len(start)):
            arr.append((finish[i], start[i]))
        arr.sort()
        finishtime = -1
        for i in range(len(arr)):
            activity = arr[i]
            if activity[1] > finishtime:
                finishtime = activity[0]
                ans += 1
        return ans
        #code here


#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        # Read the start times
        start = list(map(int, input().strip().split()))

        # Read the finish times
        finish = list(map(int, input().strip().split()))

        # Create solution object and call activitySelection
        obj = Solution()
        print(obj.activitySelection(start, finish))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends