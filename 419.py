class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        '''
        X..X
        ...X
        ...X
        '''
        x_dim = len(board[0])
        y_dim = len(board)
        #print "x : %d, y: %d\n"%(x_dim, y_dim)

        ll_traversed = [0] * x_dim * y_dim
        found, ship = 0, 0
        for y in range(y_dim):
            for x in range(x_dim):
                cur_x, cur_y = x, y
                if ll_traversed[cur_y * x_dim + cur_x] == 1: continue
                while cur_x < x_dim and board[cur_y][cur_x] == 'X':
                    ll_traversed[cur_y * x_dim + cur_x] = 1
                    cur_x += 1
                    found = 1
                cur_x = x
                while cur_y < y_dim and board[cur_y][cur_x] == 'X':
                    ll_traversed[cur_y * x_dim + cur_x] = 1
                    cur_y += 1
                    found = 1
                cur_y = y
                if found == 1: ship += 1
                found = 0
        return ship
        
