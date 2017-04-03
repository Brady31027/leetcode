class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        ans = []
        for word in words:
            line_cnt = 0
            for row_index in range(len(rows)):
                if set(word) & rows[row_index]: line_cnt += 1
                if line_cnt > 1: break
            if line_cnt == 1: ans.append(word)
        return ans
