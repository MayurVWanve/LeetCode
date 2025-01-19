from collections import deque

class Solution:
    def minCost(self, grid):
        # Dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Directions corresponding to the signs
        directions = {
            1: (0, 1),   # Right
            2: (0, -1),  # Left
            3: (1, 0),   # Down
            4: (-1, 0)   # Up
        }
        
        # BFS Queue: store (row, col, cost)
        q = deque([(0, 0, 0)])
        
        # Visited set to track visited cells
        visited = set()
        
        # Helper function to get the next cell following the grid's direction
        def move(row, col, grid_val):
            dr, dc = directions[grid_val]
            return row + dr, col + dc
        
        while q:
            # Pop the cell with the current cost
            row, col, cost = q.popleft()
            
            # If we reached the bottom-right corner, return the cost
            if (row, col) == (m - 1, n - 1):
                return cost
            
            # Skip if the cell is already visited
            if (row, col) in visited:
                continue
            visited.add((row, col))
            
            # Follow the current cell's direction
            next_row, next_col = move(row, col, grid[row][col])
            
            # If the next cell is within bounds, add it with no additional cost
            if 0 <= next_row < m and 0 <= next_col < n:
                q.appendleft((next_row, next_col, cost))
            
            # Explore all neighbors and add them with a cost of 1
            for direction, (dr, dc) in directions.items():
                neighbor_row, neighbor_col = row + dr, col + dc
                if 0 <= neighbor_row < m and 0 <= neighbor_col < n and (neighbor_row, neighbor_col) not in visited:
                    q.append((neighbor_row, neighbor_col, cost + 1))

