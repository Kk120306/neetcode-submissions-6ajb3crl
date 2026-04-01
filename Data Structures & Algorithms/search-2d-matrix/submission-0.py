class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowRow, highRow = 0, len(matrix) -1
        targetRow = -1
        while lowRow <= highRow: 
            midRow = lowRow + ((highRow - lowRow) // 2)
            if target >= matrix[midRow][0] and target <= matrix[midRow][len(matrix[0]) - 1]:
                targetRow = midRow
                break
            elif target < matrix[midRow][0]:
                highRow = midRow - 1
            else : 
                lowRow = midRow + 1
        
        if targetRow == -1: 
            return False

        low, high = 0, len(matrix[targetRow]) - 1
        while low <= high:
            mid = low + ((high-low) // 2)
            if matrix[targetRow][mid] == target:
                return True
            elif matrix[targetRow][mid] > target: 
                high = mid - 1
            else : 
                low = mid + 1
        
        return False
