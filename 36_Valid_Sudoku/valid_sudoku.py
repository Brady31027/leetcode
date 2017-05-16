class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowBook = [ set() for _ in xrange(9)]
        colBook = [ set() for _ in xrange(9)]
        gridBook = [ set() for _ in xrange(9)]
        for row in xrange(9):
            for col in xrange(9):
                if board[row][col] == '.':
                    continue
                
                grid = (row / 3) * 3 + (col / 3)
                if board[row][col] in rowBook[row] or \
                   board[row][col] in colBook[col] or \
                   board[row][col] in gridBook[grid]:
                       return False
                rowBook[row].add(board[row][col])
                colBook[col].add(board[row][col])
                gridBook[grid].add(board[row][col])
        return True
