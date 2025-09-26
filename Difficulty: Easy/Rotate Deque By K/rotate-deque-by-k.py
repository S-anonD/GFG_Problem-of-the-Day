class Solution:    
    def rotateDeque(self, dq, type, k):
        n = len(dq)
        if n == 0 or k % n == 0:
            return
        k %= n
        if type == 1:
            for i in range(k):
                dq.appendleft(dq.pop())
        else:
            for j in range(k):
                dq.append(dq.popleft())
        #code here
        
