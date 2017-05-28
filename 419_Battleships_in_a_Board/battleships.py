class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ship = 0
        for y in xrange(len(board)):
            for x in xrange(len(board[0])):
                if board[y][x] == 'X':
                    if x == 0 and y == 0 : 
                        ship += 1
                    elif x == 0 and y > 0 and board[y - 1][x] != 'X':
                        ship += 1
                    elif y == 0 and x > 0 and board[y][x - 1] != 'X':
                        ship += 1
                    elif board[y][x - 1] != 'X' and board[y - 1][x] != 'X':
                        ship += 1
        return ship
