from heapq import heappop, heappush, heappushpop


class MedianHeap:
    def __init__(self):
        self.low = []
        self.high = []

    def insert(self, num):
        heappush(self.low, -num)
        heappush(self.high, -heappop(self.low))

        if len(self.high) > len(self.low):
            heappush(self.low, -heappop(self.high))

    def get_median(self):
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return (-self.low[0] + self.high[0]) / 2
