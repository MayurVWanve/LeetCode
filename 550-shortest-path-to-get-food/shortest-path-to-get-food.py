from collections import deque
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        q = deque()
        directions = ((0,1), (0,-1), (1,0), (-1,0))
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    q.append((i,j,0))
                    visited.add((i,j))
                    break

        
        while q:
            row, col, cost = q.popleft()
            if grid[row][col] == "#":
                return cost
            
            for x, y in directions:
                new_row, new_col = row + x, col + y
                if 0 <= new_row < m and 0 <= new_col < n and (new_row, new_col) not in visited \
                and grid[new_row][new_col] != "X":
                    q.append((new_row, new_col, cost + 1))
                    visited.add((new_row, new_col))

        
        return -1
        