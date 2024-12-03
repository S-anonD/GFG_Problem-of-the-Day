class Solution:
    def minChar(self, s):
        n = len(s)
        rev = s[::-1]
        s += "$" + rev
        lps = self.computeLPSArray(s)
        return n - lps[-1]
        #Write your code here
    
    def computeLPSArray(self, pat):
        n = len(pat)
        lps = [0] * n
        len_lps = 0
        i = 1
        while i < n:
            if pat[i] == pat[len_lps]:
                len_lps += 1
                lps[i] = len_lps
                i += 1
            else:
                if len_lps != 0:
                    len_lps = lps[len_lps - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends