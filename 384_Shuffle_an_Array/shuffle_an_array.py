class Solution(object):
    
    workingNums = []
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.workingNums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.workingNums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        shuffleNums = list(self.workingNums)
        arrSize = len(shuffleNums)
        for i in xrange(arrSize):
            anchor = random.randint(i, arrSize - 1)
            shuffleNums[i], shuffleNums[anchor] = shuffleNums[anchor], shuffleNums[i]
        return shuffleNums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
