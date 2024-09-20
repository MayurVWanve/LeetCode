from heapq import heappop, heappush

class MedianFinder:

    def __init__(self):
        self.minheap, self.maxheap = [], []


    def addNum(self, num: int) -> None:
        #Add a number to the minHeap by defaut and then balance
        heappush(self.maxheap, -1*num)
        
        if self.minheap and self.maxheap and (-1 * self.maxheap[0] > self.minheap[0]):
            ele = -1 * heappop(self.maxheap)
            heappush(self.minheap, ele)
        
            if len(self.minheap) > 1 + len(self.maxheap):
                ele = heappop(self.minheap)
                heappush(self.maxheap, -1 * ele)
            
        if len(self.maxheap) > 1 + len(self.minheap):
                ele = heappop(self.maxheap)
                heappush(self.minheap, -1 * ele)
       
        

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        
        if len(self.minheap) < len(self.maxheap):
            return (-1 * self.maxheap[0])

        return (self.minheap[0] + (-1 * self.maxheap[0])) / 2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()