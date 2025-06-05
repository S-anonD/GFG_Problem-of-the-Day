class Solution:
    def search(self, pat, txt):
        d = 256  
        q = 101
        M = len(pat)
        N = len(txt)
        p = 0  
        t = 0  
        h = 1  
        ans = []
        for i in range(M - 1):
            h = (h * d) % q
        for i in range(M):
            p = (d * p + ord(pat[i])) % q
            t = (d * t + ord(txt[i])) % q
        for i in range(N - M + 1):
            if p == t:
                match = True
                for j in range(M):
                    if txt[i + j] != pat[j]:
                        match = False
                        break
                if match:
                    ans.append(i + 1)
            if i < N - M:
                t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
                if t < 0:
                    t += q
        return ans
        # code here