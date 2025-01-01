#User function Template for python3


class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        if len(arr) == 1:
            return [arr]
        lex = []
        n, i = len(arr), 0
        while i < n:
            e, j = arr[i], i
            arr.remove(e)
            new = [e]
            n = len(arr)
            while j < n:
                if sorted(arr[j]) == sorted(e):
                    new.append(arr[j])
                    arr.remove(arr[j])
                    n = len(arr)
                else:
                    j += 1
            lex.append(new)
            n = len(arr)
        return lex
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends