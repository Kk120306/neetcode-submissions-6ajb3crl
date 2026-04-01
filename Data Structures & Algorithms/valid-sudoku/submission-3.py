class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        rowTables = [set() for _ in range(length)]
        colTables = [set() for _ in range(length)]
        boxTables = [set() for _ in range(length)]

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == '.':
                    continue

                boxIndex = (i // 3) * 3 + (j // 3)
                if num in rowTables[i] or num in colTables[j] or num in boxTables[boxIndex]:
                    return False
                else:
                    rowTables[i].add(num)
                    colTables[j].add(num)
                    boxTables[boxIndex].add(num)

        
        return True
               
                 

