class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        height, width = len(board), len(board[0])
        for y in xrange(height):
            for x in xrange(width):
                neighbors = 0
                # enum all 9 cases
                if x > 0 and y > 0 and x + 1 < width and y + 1 < height:
                    neighbors = sum([board[y-1][x-1] & 1, board[y-1][x] & 1, board[y-1][x+1] & 1, \
                                    board[y][x-1] & 1, board[y][x+1] & 1, board[y+1][x-1] & 1, \
                                    board[y+1][x] & 1, board[y+1][x+1] & 1 ])
                elif x > 0 and y > 0 and x + 1 < width and y + 1 >= height:
                    neighbors = sum([board[y-1][x-1] & 1, board[y-1][x] & 1, board[y-1][x+1] & 1, \
                                    board[y][x-1] & 1, board[y][x+1] & 1 ])
                elif x > 0 and y > 0 and x + 1 >= width and y + 1 < height:
                    neighbors = sum([board[y-1][x-1] & 1, board[y-1][x] & 1, board[y][x-1] & 1, \
                                    board[y+1][x-1] & 1, board[y+1][x] & 1])
                elif x > 0 and y <= 0 and x + 1 < width and y + 1 < height:
                    neighbors = sum([board[y][x-1] & 1, board[y][x+1] & 1, board[y+1][x-1] & 1, \
                                    board[y+1][x] & 1, board[y+1][x+1] & 1])
                elif x <= 0 and y > 0 and x + 1 < width and y + 1 < height:
                    neighbors = sum([board[y-1][x] & 1, board[y-1][x+1] & 1, board[y][x+1] & 1, \
                                    board[y+1][x] & 1, board[y+1][x+1] & 1])
                elif x > 0 and y > 0 and x + 1 >= width and y + 1 >= height:
                    neighbors = sum([board[y-1][x-1] & 1, board[y-1][x] & 1, board[y][x-1] & 1])
                elif x > 0 and y <= 0 and x + 1 >= width and y + 1 < height:
                    neighbors = sum([board[y][x-1] & 1, board[y+1][x-1] & 1, board[y+1][x] & 1])
                elif x <= 0 and y <= 0 and x + 1 < width and y + 1 < height:
                    neighbors = sum([board[y][x+1] & 1, board[y+1][x+1] & 1, board[y+1][x] & 1])
                elif x <= 0 and y > 0 and x + 1 < width and y + 1 >= height:
                    neighbors = sum([board[y-1][x] & 1, board[y-1][x+1] & 1, board[y][x+1] & 1])
                # mark with (next_gen << 1 | current_gen)
                if (board[y][x] == 1 and (neighbors >= 2 and neighbors <= 3)) or \
                   (board[y][x] == 0 and neighbors == 3):
                       board[y][x] |= 1 << 1
                
        for y in xrange(height):
            for x in xrange(width):
                board[y][x] = board[y][x] >> 1
        
