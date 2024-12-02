#User function Template for python3

class Solution:
    def search(self, pat, txt):
        occurred = []
        t = len(txt)
        p = len(pat)
        for i in range(t-p+1):
            if txt[i:i+p] == pat:
                occurred.append(i)
        return occurred
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends