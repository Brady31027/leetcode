class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        head, tail, max_area = 0, len(height) - 1, 0
        while head < tail:
            min_height = height[head] if height[head] <= height[tail] else height[tail]
            area = (tail - head) * min_height
            if min_height == height[head]:
                head += 1 
            else:
                tail -= 1
            max_area = max(max_area, area)
        return max_area
