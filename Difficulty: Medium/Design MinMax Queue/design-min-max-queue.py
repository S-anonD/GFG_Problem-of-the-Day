class SpecialQueue:
    def __init__(self):
        # Define Data Structures
        self.q = deque()
        self.mn = deque()
        self.mx = deque()

    
    def enqueue(self, x):
        # Insert element into the queue
        self.q.append(x)
        while self.mn and self.mn[-1] > x: 
            self.mn.pop()
        self.mn.append(x)
        while self.mx and self.mx[-1] < x: 
            self.mx.pop()
        self.mx.append(x)

    
    def dequeue(self):
        # Remove element from the queue
        f = self.q.popleft()
        if f == self.mn[0]: 
            self.mn.popleft()
        if f == self.mx[0]: 
            self.mx.popleft()

    
    def getFront(self):
        # Get front element
        return self.q[0]

    
    def getMin(self):
        # Get minimum element
        return self.mn[0]

    
    def getMax(self):
        # Get maximum element
        return self.mx[0]

    

from collections import deque