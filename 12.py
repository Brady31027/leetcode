class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict_roman = {1000:"M", 900:"CM", 500:"D",400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        list_roman = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ret = ""
        for div in list_roman:
            if num >= div:
                repeat_cnt = num / div
                num = num % div
                for repeat_idx in range(repeat_cnt):
                    ret += dict_roman[div]
        return ret
