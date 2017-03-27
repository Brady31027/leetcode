class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if beginWord == endWord: return 1
        queue_top, queue_bottom, word_dict = set([beginWord]), set([endWord]), set(wordList)
        word_length, depth, char_set = len(beginWord), 2, string.lowercase[:]
        if endWord not in word_dict: return 0
        while queue_top:
            queue_bak = set()
            for word in queue_top:
                for i in range(word_length):
                    for char in char_set:
                        candidate = word[:i] + char + word[i+1:]
                        if candidate in queue_bottom: return depth
                        if candidate in word_dict: queue_bak.add(candidate)
            queue_top = queue_bak
            if len(queue_top) > len(queue_bottom):
                queue_top, queue_bottom = queue_bottom, queue_top
            depth += 1
            word_dict -= queue_top
        return 0
