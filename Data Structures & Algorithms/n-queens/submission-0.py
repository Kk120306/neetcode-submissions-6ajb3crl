class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Use the first row and iterate n times, 
        # Since no queen can be on the same row once we find one suitable 
        # we can skip to the next row
        # For each box in the row until found, verify cur queens cannot hit
        # If cannot place then go the next row. 
        # Once we have n queens we can append result
        # else we can exit as false if we reach end of list without n queens 

        # For check we have only col and diagnal since row is skipped once found 
        res = []

        def dfs(positions, cur, i, j):
            if i == n:
                res.append(cur.copy())
                return
            if j == n:
                return 
            
            if self.verifyValid(positions, i, j):
                positions.append((i,j))
                cur.append("."*j + "Q" + "."*(n-(j + 1)))
                dfs(positions, cur, i + 1, 0)
                cur.pop()
                positions.pop()
            
            dfs(positions, cur, i, j+1)
        
        dfs([],[], 0, 0)
        return res




    
    # Tuple has x,y. i,j is pos we are verifying
    def verifyValid(self, positions: List[Tuple[int, int]], i: int, j: int) -> bool:
        for x, y in positions:
            if j == y or (abs(i - x) == abs(j - y)):
                return False
        return True
            

