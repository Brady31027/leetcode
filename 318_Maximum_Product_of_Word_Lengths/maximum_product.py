class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        wordHash = {} # mappingNumber: lenghOfWord
        for word in words:
            mappingNumber = 0
            for c in set(word):
                mappingNumber |= 1 << ord(c) - 97
            wordHash[mappingNumber] = max( wordHash.get(mappingNumber, 0), len(word) )
        
        maxLength = 0
        for mappingNumber1 in wordHash:
            for mappingNumber2 in wordHash:
                if not mappingNumber1 & mappingNumber2:
                    maxLength = max( wordHash[mappingNumber1] * wordHash[mappingNumber2], maxLength)
        return maxLength
