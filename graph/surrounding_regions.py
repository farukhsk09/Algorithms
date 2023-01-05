# 130. Surrounded Regions
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visit = set()
        row,col = len(board),len(board[0])
        def dfs(r, c):
            if (
                r not in range(row)
                or c not in range(col)
                or board[r][c] == "X"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        # 0,0 0,1 0,n 
        # 1,0     1,n
        # n,0 n,1 n,n
        #top
        for r in [0,row-1]:
            for c in range(col):
                if board[r][c] == 'O' and (r,c) not in visit:
                    dfs(r,c)
        # bottom
        for c in [0,col-1]:
            for r in range(row):
                if board[r][c] == 'O' and (r,c) not in visit:
                    dfs(r,c)
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O' and (r,c) not in visit:
                    board[r][c]='X'
        return