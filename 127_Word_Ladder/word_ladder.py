class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if beginWord == endWord: return 1
        queue = [(beginWord,1)]
        while queue:
            item = queue.pop(0)
            word, depth = item[0], item[1]
            if word == endWord: return depth
            for i in range(len(word)):
                for char in string.lowercase[:]:
                    candidate = word[:i] + char + word[i+1:]
                    if candidate in wordList:
                        wordList.remove(candidate)
                        queue.append((candidate, depth+1))
        return 0
