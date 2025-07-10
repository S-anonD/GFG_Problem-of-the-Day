class Solution:
    def countConsec(self, n: int) -> int:
        prev0, prev1 = 1, 1
        for i in range(2, n + 1):
            curr0 = prev0 + prev1
            curr1 = prev0
            prev0, prev1 = curr0, curr1
        total = 1 << n
        noConsec = prev0 + prev1
        consec = total - noConsec
        return consec
        # code here 
        