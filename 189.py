class Solution(object):
    
    """
    input : 1, 2, 3, 4, 5 (k = 3)
    output: 3, 4, 5, 1, 2
    algorithm:
      (1) reverse second half: 1, 2, 5, 4, 3
      (2) reverse first half : 2, 1, 5, 4, 3
      (3) reverse all: 3, 4, 5, 1, 2
    """
    def rev(self, l_n, head, tail):
            while head < tail:
                l_n[head], l_n[tail] = l_n[tail], l_n[head]
                head, tail = head + 1, tail - 1
        
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if k == 0: return
        k %= size # prevent circular shift
        self.rev(nums, size-k, size-1)
        self.rev(nums, 0, size-k-1)
        self.rev(nums, 0, size-1)
