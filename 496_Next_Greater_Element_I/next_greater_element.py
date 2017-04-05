class Solution(object):
    
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        memo, stack = {}, []
        for n in nums:
            while len(stack) and stack[-1] < n:
                memo[stack[-1]] = n
                stack.pop()
            stack.append(n)
        ans = []
        for n in findNums:
            next_greater_element = memo.get(n)
            ans.append(next_greater_element if next_greater_element else -1)
        return ans
