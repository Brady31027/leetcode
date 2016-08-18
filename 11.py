class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max, size = 0, len(height)
        head, tail = 0, size - 1
        while head < tail:
            area =  (tail - head) * min(height[head], height[tail])
            if area > max: max = area
            if height[head] <= height[tail]: head += 1
            else: tail -= 1
        return max
