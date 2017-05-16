class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isValid(inputList):
            outputList = filter(lambda x: x != '.', inputList)
            return True if len(set(outputList)) == len(outputList) else False
        
        # check rows and columns    
        for i in xrange(9):
            if not isValid( [ board[i][j] for j in xrange(9)] ) \
                or not isValid(board[j][i] for j in xrange(9) ):
                    return False
                    
        # check grid
        for bigRow in xrange(3):
            for bigCol in xrange(3):
                if not isValid( [ board[row][col] for row in xrange(bigRow * 3, bigRow * 3 + 3) \
                                                  for col in xrange(bigCol * 3, bigCol * 3 + 3) ] ):
                    return False    
        return True
                    
        
     
            
