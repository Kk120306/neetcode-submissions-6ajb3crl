class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        MOVES = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROW or c == COL or board[r][c] != "O"):
                return
            board[r][c] = "#"
            for dr, dc in MOVES:
                dfs(dr + r, dc + c)
            
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O" and (r in [0, ROW - 1] or c in [0, COL - 1]):
                    dfs(r, c)
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
    
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "#":
                    board[r][c] = "O"
        


    
