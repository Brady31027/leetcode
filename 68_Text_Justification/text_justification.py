class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        start, end = 0, 0
        accumulatedLength = 0
        ans, tmp = [], []
        
        def addSpacesAndConvertToString(wordList, numberOfMissingSpaces, lastToken):
            i, listLen = 0, len(wordList) - 1 # don't add space to the last token
            numberOfMissingSpaces += listLen
            
            if listLen == 0:
                return wordList[0] + " " * numberOfMissingSpaces
            elif lastToken: # For the last line, it should be left justified and no extra space is inserted between words
                return " ".join(wordList) + (" " * (numberOfMissingSpaces - len(wordList) + 1) ) 
            else:
                while i < numberOfMissingSpaces:
                    index = i % listLen
                    wordList[index] = wordList[index] + " "
                    i += 1
                return "".join(wordList)
        
        for i in xrange(len(words)):
            if accumulatedLength + len(words[i]) + 1 > maxWidth:
                if not tmp: # one word ocupies the whole line
                    tmp.append(words[i])
                    accumulatedLength = len(words[i])
                    line = addSpacesAndConvertToString(tmp, maxWidth - accumulatedLength, True)
                    accumulatedLength, tmp = 0, []
                else:
                    line = addSpacesAndConvertToString(tmp, maxWidth - accumulatedLength, False)
                    accumulatedLength, tmp = len(words[i]), [ words[i] ]
                ans.append(line)
            else:
                if len(tmp) == 0:
                    accumulatedLength += len(words[i])
                else:
                    accumulatedLength += len(words[i]) + 1
                tmp.append(words[i])
            
        # for the last line
        if tmp:
            line = addSpacesAndConvertToString(tmp, maxWidth - accumulatedLength, True)
            ans.append(line)
        return ans
