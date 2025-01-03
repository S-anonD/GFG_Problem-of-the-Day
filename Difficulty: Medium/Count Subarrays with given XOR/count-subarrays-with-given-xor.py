class Solution:
    def subarrayXor(self, arr, k):
        count = 0
        mp = {}
        prefXOR = 0
        for val in arr:
            prefXOR ^= val
            count += mp.get(prefXOR ^ k, 0)
            if prefXOR == k:
                count += 1
            mp[prefXOR] = mp.get(prefXOR, 0) + 1
        return count
        # code here


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends