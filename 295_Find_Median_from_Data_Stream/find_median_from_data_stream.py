class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # case 1: len(sm) == len(bi)
        # case 2: len(sm) == len(bi) - 1
        # heap_sm stores numbers in the smaller half
        # heap_bi stores numbers in the larger half
        self.heapSm = []
        self.heapBi = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # case 1: len(sm) == len(bi)
        #   push input number to heap_sm and find the largest element in heap_sm and push to heap_bi
        # case 2: len(sm) == len(bi) - 1
        #   push input number to heap_bi and find the smallest element in heap_bi and push to heap_sm
        # for case1, we need to find the largest element in heap_sm, but what we have is a min-heap.
        # Therefore we need to save the input number after negating it.
        # E.g input: 5, 10. By negating them, they will become -5 and -10, in that case, ...
        #     the largest element will be represented as the smallest element
        if len(self.heapSm) == len(self.heapBi):
            heapq.heappush(self.heapBi, -heapq.heappushpop(self.heapSm, -num))
        else:
            heapq.heappush(self.heapSm, -heapq.heappushpop(self.heapBi, num))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.heapSm) == len(self.heapBi):
            return (self.heapBi[0] - self.heapSm[0]) / 2.0
        else:
            return self.heapBi[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
