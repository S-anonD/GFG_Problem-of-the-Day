# 07/11/24
# Split array in three equal sum subarrays

def findSplit(self, arr):
        tsum = sum(arr)
        if tsum%3 != 0:
            return [-1, -1]
        
        i, s1 = 0, 0
        target = tsum//3
        res = []
        
        while i < len(arr) and s1 < target:
            s1 += arr[i]
            i += 1
        if s1 == target:
            if i == 0:
                res.append(i)
            else:
                res.append(i-1)
        else:
            return [-1, -1]
        
        s1 = 0
        while i<len(arr) and s1<target:
            s1 += arr[i]
            i += 1
        if s1 == target:
            if i != 0:
                res.append(i-1)
            else:
                res.append(i)
        else:
            return [-1, -1]
        
        return res