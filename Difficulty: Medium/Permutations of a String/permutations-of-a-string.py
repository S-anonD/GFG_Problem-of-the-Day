#User function Template for python3

class Solution:
    def findPermutation(self, s):
        used = [False] * len(s)
        st = set()
        curr = []
        self.genPermutation(0, s, used, curr, st)
        return list(st)
    
    def genPermutation(self, i, s, used, curr, st):
        if i == len(s):
            st.add("".join(curr))
            return
        for j in range(len(s)):
            if not used[j]:
                used[j] = True
                curr.append((s[j]))
                self.genPermutation(i+1, s, used, curr, st)
                used[j] = False
                curr.pop()
        # Code here
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends