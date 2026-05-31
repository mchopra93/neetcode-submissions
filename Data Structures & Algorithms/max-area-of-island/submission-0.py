class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid or len(grid) == 0:
            return 0
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])

        def traversal(r,c):
            
            if r < 0 or r >=rows or c<0 or c>=cols or grid[r][c]==0:
                return 0
            
            # mark visited by sinking the land:
            grid[r][c] = 0

            return 1 + (
                        traversal(r + 1, c) +
                        traversal(r - 1, c) +
                        traversal(r, c + 1) +
                        traversal(r, c - 1)
                    )
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count = traversal(r,c)
                    if count > maxArea:
                        maxArea = count
        return maxArea

            
