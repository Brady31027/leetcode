class Solution(object):
    def maximalSquare(self, matrix):
        if len(matrix) < 2:
            if len(matrix) == 0: return 0
            if len(matrix) == 1: return 1 if '1' in matrix[0] else 0
            
        size_y, size_x = len(matrix), len(matrix[0])
        max_valid_length = 0
        
        dp = [[0 for _ in range(size_x)] for _ in range(size_y)]
        for y in range(size_y):
            for x in range(size_x):
                dp[y][x] = int(matrix[y][x])
                if y and x and dp[y][x] == 1:
                    dp[y][x] = min(dp[y-1][x-1], dp[y-1][x], dp[y][x-1]) + 1
                max_valid_length = max(max_valid_length, dp[y][x])
        return max_valid_length * max_valid_length
