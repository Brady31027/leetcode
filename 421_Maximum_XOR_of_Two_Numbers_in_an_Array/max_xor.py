class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, mask = 0, 0
        for bit in range(31, -1, -1):
            mask = mask | (1 << bit) # 1000, 1100, 1110, 1111
            candidates = set([ num & mask for num in nums])
            guess = ans | (1 << bit)
            for candidate in candidates:
                # if    a ^ tmp = b
                # then  a ^  b  = tmp
                if candidate ^ guess in candidates:
                    ans = guess
                    break
        return ans
                
