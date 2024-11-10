# 10/11/24
# Union of Two Sorted Arrays with Distinct Elements

def findUnion(self,a,b):
        res = []
        i, j = 0, 0
        n, m = len(a), len(b)

        while i < n and j < m:
            if a[i] < b[j]:
                res.append(a[i])
                i += 1
            elif a[i] > b[j]:
                res.append(b[j])
                j += 1
            else:
                res.append(a[i])
                i += 1
                j += 1
        while i < n:
            res.append(a[i])
            i += 1
        while j < m:
            res.append(b[j])
            j += 1

        return res