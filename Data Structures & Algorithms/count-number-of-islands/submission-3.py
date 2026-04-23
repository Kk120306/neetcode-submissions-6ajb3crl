class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        visited = set() # tuple of x,y
        numOfIsland = 0 

        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                curr_r, curr_c = q.pop()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    new_r, new_c = curr_r + dr, curr_c + dc
                    if (new_r in range(row) and 
                        new_c in range(col) and 
                        (new_r, new_c) not in visited and
                        grid[new_r][new_c] == "1"):
                        visited.add((new_r, new_c))
                        q.append((new_r, new_c))
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    numOfIsland += 1
        
        return numOfIsland