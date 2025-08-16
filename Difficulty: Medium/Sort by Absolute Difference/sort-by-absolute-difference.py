class Solution:
    def rearrange(self, arr, x):
        n = len(arr)
        arr.sort(key = lambda a: abs(a - x))
        # code here
        
        