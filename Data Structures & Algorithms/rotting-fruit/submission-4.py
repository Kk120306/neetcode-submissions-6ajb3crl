class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()
        

        def visit(r, c):
            nonlocal flag
            if (r < 0 or r == ROW or c == COL or c < 0 or (r, c) in visited):
                return 
            visited.add((r,c))
            if grid[r][c] == 1:
                flag = True
                q.append([r, c])
                grid[r][c] = 2


        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visited.add((r, c))
        
        time = 0 
        while q:
            flag = False
            for i in range(len(q)):
                r, c = q.popleft()
                visit(r + 1, c)
                visit(r - 1, c)
                visit(r, c + 1)
                visit(r, c - 1)
            if flag:
                time += 1



        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    return -1
        return time