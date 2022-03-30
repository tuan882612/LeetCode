class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        def convert(index, matrix):
            row = index // len(matrix[0])
            col = index % len(matrix[0])
            
            return row,col
        
        
        low, high = 0, len(matrix[0]) * len(matrix)
        
        while low < high:
            mid = low + (high - low) // 2
            row_col = convert(mid, matrix)
            
            if matrix[row_col[0]][row_col[1]] == target:
                return True
            
            elif matrix[row_col[0]][row_col[1]] < target:
                low = mid + 1
                
            else:
                 high = mid
                    
        return False