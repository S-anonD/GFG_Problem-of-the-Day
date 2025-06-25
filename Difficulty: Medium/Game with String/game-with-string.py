class Solution:
    def minValue(self, s, k):
        n = len(s)
        alphabetCount = [0] * 26
        maxi = 0
        for c in s:
            alphabetCount[ord(c) - ord('a')] += 1
            maxi = max(maxi, alphabetCount[ord(c) - ord('a')])
        maxFreq = 0
        freq = [0] * (maxi + 1)
        for count in alphabetCount:
            if count > 0:
                freq[count] += 1
                maxFreq = max(maxFreq, count)
        while k > 0 and maxFreq > 0:
            count_at_max = freq[maxFreq]
            if count_at_max <= k:
                k -= count_at_max
                freq[maxFreq - 1] += count_at_max
                freq[maxFreq] = 0
                maxFreq -= 1
            else:
                freq[maxFreq] -= k
                freq[maxFreq - 1] += k
                k = 0
        res = 0
        for i in range(1, maxi + 1):
            res += i * i * freq[i]
        return res
        #code here