class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "Zero"
        
        digitTbl = { 0 : "Zero", 1 : "One", 2 : "Two", 3 : "Three", 4 : "Four", 5 : "Five", \
                6 : "Six", 7 : "Seven", 8 : "Eight", 9 : "Nine", 10 : "Ten", \
                11 : "Eleven", 12 : "Twelve", 13 : "Thirteen", 14 : "Fourteen", 15 : "Fifteen", 16 : "Sixteen", \
                17 : "Seventeen", 18 : "Eighteen", 19 : "Nineteen", 20 : "Twenty", 30 : "Thirty", \
                40 : "Forty", 50 : "Fifty", 60 : "Sixty", 70 : "Seventy", 80 : "Eighty", 90 : "Ninety" }
        unitTbl = ["", "Thousand", "Million", "Billion"]
        
        def threeDigitsToWords(num, unit):
            threeDigitWords = []
            if num // 100 > 0:
                threeDigitWords.append(digitTbl[num // 100] + " Hundred")
            if num % 100 > 0:
                threeDigitWords.append( twoDigits(num % 100) )
            if unit > 0:
                threeDigitWords.append( unitTbl[unit])
            return " ".join(threeDigitWords)
        
        def twoDigits(num):
            if num in digitTbl:
                return digitTbl[num]
            return digitTbl[ num // 10 * 10] + " " + digitTbl[num % 10]
        
        reversedDigitWords, unitIndex = [], 0
        while num > 0:
            lastThreeDigits = num % 1000
            if lastThreeDigits > 0:
                reversedDigitWords.append( threeDigitsToWords(lastThreeDigits, unitIndex) )
            num, unitIndex = num // 1000, unitIndex + 1
        return " ".join(reversed(reversedDigitWords))
            
            
