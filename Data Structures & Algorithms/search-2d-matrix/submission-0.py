class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        columns = len(matrix[0])
        low = 0
        high = (rows * columns) - 1

        while low<=high:
            mid = (low+high) // 2
            row =  mid // columns
            column = mid % columns
            
            mid_val = matrix[row][column]
            if target == mid_val:
                return True
            if mid_val < target:
                low = mid + 1
            else:
                high = mid - 1
            
        return False






        