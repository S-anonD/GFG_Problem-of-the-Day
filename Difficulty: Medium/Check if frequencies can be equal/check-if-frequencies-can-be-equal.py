from collections import Counter

class Solution:
    def sameFreq(self, s: str) -> bool:
        char_freq = Counter(s)
        freq_count = Counter(char_freq.values())
        if len(freq_count) == 1:
            return True
        if len(freq_count) == 2:
            (f1, c1), (f2, c2) = sorted(freq_count.items())
            if f1 == 1 and c1 == 1:
                return True
            if f2 == f1 + 1 and c2 == 1:
                return True
            return False
        return False
        #code here