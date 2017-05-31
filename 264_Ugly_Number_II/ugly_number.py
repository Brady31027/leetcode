class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap, val = [1], 1
        heapq.heapify(heap)
        for i in xrange( n):
            val = heapq.heappop(heap)
            if val % 2 == 0:
                heapq.heappush(heap, val * 2)
            elif val % 3 == 0:
                heapq.heappush(heap, val * 2)
                heapq.heappush(heap, val * 3)
            else:
                heapq.heappush(heap, val * 2)
                heapq.heappush(heap, val * 3)
                heapq.heappush(heap, val * 5)
        return val
