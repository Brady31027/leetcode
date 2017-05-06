class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missingOne, missingTwo = None, None
        nums.sort()
        for num in nums:
            if num == missingOne:
                missingOne = None
                continue
            elif num == missingTwo:
                missingTwo = None
                continue
            else:
                if missingOne == None:
                    missingOne = num
                elif missingTwo == None:
                    missingTwo = num
                else:
                    return [missingOne, missingTwo]
        return [missingOne, missingTwo]
