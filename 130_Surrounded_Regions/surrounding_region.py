class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return
        size_y, size_x = len(board), len(board[0])
        queue = []
        
        def flooding(y, x):
            if y >= size_y or y < 0 or x >= size_x or x < 0 or board[y][x] != 'O': return
            queue.append((y, x))
            board[y][x] = 'F'
            
        def bfs(y, x):
            flooding(y, x)
            while queue:
                (entry_y, entry_x) = queue.pop()
                flooding(entry_y+1, entry_x)
                flooding(entry_y-1, entry_x)
                flooding(entry_y, entry_x+1)
                flooding(entry_y, entry_x-1)
            
        for y in range(size_y):
            if board[y][0] == 'O': bfs(y, 0)
            if board[y][-1] == 'O': bfs(y, size_x -1 )
        for x in range(size_x):
            if board[0][x] == 'O': bfs(0, x)
            if board[-1][x] == 'O': bfs(size_y - 1, x)
        
        for y in range(size_y):
            for x in range(size_x):
                if board[y][x] == 'O': board[y][x] = 'X'
                elif board[y][x] == 'F': board[y][x] = 'O'
        
