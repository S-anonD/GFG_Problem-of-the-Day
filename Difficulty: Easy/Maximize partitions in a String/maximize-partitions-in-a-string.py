class Solution:
    def maxPartitions(self , s):
        first = [-1] * 26
        last = [-1] * 26
        for i in range(len(s)):
            if first[ord(s[i]) - ord('a')] == -1:
                first[ord(s[i]) - ord('a')] == i
            last[ord(s[i]) - ord('a')] = i
        count = 0
        end = 0
        for i in range(len(s)):
            end = max(end, last[ord(s[i]) - ord('a')])
            if i == end:
                count += 1
        return count
        # code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        s = input()
        obj = Solution()
        print(obj.maxPartitions(s))
        print("~")

# } Driver Code Ends