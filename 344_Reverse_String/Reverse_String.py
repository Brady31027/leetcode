class Solution(object):
    def reverseString(self, s):
        # return s[::-1]
        charList = list(s)
        head, tail = 0, len(charList) - 1
        while head < tail:
            charList[head], charList[tail] = charList[tail], charList[head]
            head, tail = head + 1, tail - 1
        return "".join(charList)
