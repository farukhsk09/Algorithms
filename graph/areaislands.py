# https://leetcode.com/problems/max-area-of-island/solutions/3013443/one-variable-more-from-the-number-of-islands-problem-solution-python/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        # dfs
        area=0
        rows,cols = len(grid),len(grid[0])
        maxArea=0
        visit=set()

        def dfs(r,c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == 0
                or (r,c) in visit
            ):
                return
            visit.add((r,c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visit and grid[i][j] == 1:
                    area = len(visit)
                    dfs(i,j)
                    if maxArea < len(visit) - area :
                        maxArea = len(visit) - area
        return maxArea