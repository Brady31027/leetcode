class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        primes.sort()
        heap, val = [1], 1
        heapq.heapify(heap)
        
        for x in xrange(n):
            matchCase, val = False, heapq.heappop(heap)
            
            for i in xrange(len(primes)):
                if val % primes[i] == 0:
                    matchCase = True
                    for j in xrange(0, i + 1):
                        heapq.heappush(heap, val * primes[j])
                    break
                        
            if matchCase == False:
                for i in xrange(0, len(primes)):
                    heapq.heappush(heap, val * primes[i])
        return val
                
            
        
