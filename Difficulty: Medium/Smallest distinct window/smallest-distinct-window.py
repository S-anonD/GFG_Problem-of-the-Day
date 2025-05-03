#User function Template for python3

class Solution:
    def findSubString(self, str):
        n = len(str)
        visited = [False] * 26
        distinct = 0
        for i in range(n):
            if visited[ord(str[i]) - ord('a')] == False:
                visited[ord(str[i]) - ord('a')] = True
                distinct += 1
        curr = [0] * 26
        cnt = 0
        ans = n
        start = 0
        for i in range(n):
            curr[ord(str[i]) - ord('a')] += 1
            if curr[ord(str[i]) - ord('a')] == 1:
                cnt += 1
            while cnt == distinct:
                ans = min(ans, i - start + 1)
                curr[ord(str[start]) - ord('a')] -= 1
                if curr[ord(str[start]) - ord('a')] == 0:
                    cnt -= 1
                start += 1
        return ans
        # code here
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):
        str = input()
        ob = Solution()
        print(ob.findSubString(str))

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends