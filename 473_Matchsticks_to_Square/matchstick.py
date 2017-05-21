class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sumNums = sum(nums)
        sideLength = sumNums / 4
        lenNums = len(nums)
        
        if lenNums < 4 or sumNums % 4 != 0 or max(nums) > sideLength:
            return False
        
        def dfs(nums, pos, target):
            if lenNums == pos: return True
            for i in xrange(4):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(nums, pos + 1, target): return True
                    target[i] += nums[pos]
            return False
            
        nums.sort(reverse=True) # from large to small
        target = [sideLength] * 4 # [sideLength, sideLength, sideLength, sideLength]
        return dfs(nums, 0, target)
