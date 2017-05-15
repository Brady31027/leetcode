class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def getNext(nums, i):
            return (i + nums[i]) % len(nums)
            
        for i in xrange(len(nums)):
            
            if nums[i] == 0: continue 
            
            slow, fast = i, i
            while nums[i] * nums[ getNext(nums, slow) ] > 0 and \
                  nums[i] * nums[ getNext(nums, fast) ] > 0 and \
                  nums[i] * nums[ getNext(nums, getNext(nums, fast)) ] > 0:
                slow = getNext(nums, slow)
                fast = getNext(nums, getNext(nums, fast))
                if slow == fast: # fast meets slow, could be a circle
                    # it's not a circle if there is only one element    
                    if slow == getNext(nums, slow): break
                    return True
                    
            # reset slow and mark all visited node to 0
            slow, val = i, nums[i]
            while nums[slow] * val > 0:
                nextNode = getNext(nums, slow)
                nums[slow] = 0
                slow = nextNode
                
        return False
