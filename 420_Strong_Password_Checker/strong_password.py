class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        upperList, lowerList, digitList, totalCnt = [], [], [], len(s)
        for c in s:
            if c.isupper(): upperList.append(c)
            elif c.islower(): lowerList.append(c)
            elif c.isdigit(): digitList.append(c)
        typeCnt = sum( len(l) > 0 for l in [upperList, lowerList, digitList])
        repeatCnt =  [ len(match[0]+match[1]) for match in re.findall(r'(.)(\1{2,})', s) ]
        
        if totalCnt < 6:
            return max(6 - totalCnt, 3 - typeCnt)

        deleteCnt = max(totalCnt - 20, 0)
        heap = [(r % 3, r) for r in repeatCnt]
        heapq.heapify(heap)
        while heap and totalCnt > 20:
            mod, r = heapq.heappop(heap)
            # mod = 0: remove 1 char, e.g. aaa
            # mod = 1: remove 2 char, e.g. aaaa
            # mod = 2: remove 3 char, e.g. aaaaa
            delta = min(mod + 1, totalCnt - 20)
            totalCnt -= delta
            heapq.heappush(heap, (2, r - delta))
        changeCnt = sum(r // 3 for mod, r in heap)
        return deleteCnt + max(changeCnt, 3 - typeCnt)
            
