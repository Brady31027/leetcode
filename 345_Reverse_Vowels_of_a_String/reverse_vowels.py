class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        stringList = list(s)
        head, tail = 0, len(stringList) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} #set
        while head < tail:
            if stringList[head] not in vowels: head += 1
            if stringList[tail] not in vowels: tail -= 1
            if head < tail and stringList[head] in vowels and stringList[tail] in vowels:
                stringList[head], stringList[tail] = stringList[tail], stringList[head]
                head, tail = head + 1, tail - 1
        return "".join(stringList)
