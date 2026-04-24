class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set() # tuple of r, c 
        maxArea = 0

        def bfs(r, c):
            q = collections.deque() 
            visited.add((r, c))
            q.append((r, c))
            area = 1

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while q:
                current_row, current_col = q.pop()
                for dr, dc in directions:
                    new_r, new_c = current_row + dr, current_col + dc

                    if (new_r in range(rows) and 
                        new_c in range(cols) and 
                        (new_r, new_c) not in visited and
                        grid[new_r][new_c] == 1):
                        area += 1
                        visited.add((new_r, new_c))
                        q.append((new_r, new_c))
            
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = bfs(r,c)
                    maxArea = max(area, maxArea)

        return maxArea
