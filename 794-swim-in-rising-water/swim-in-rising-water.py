from heapq import heappop, heappush, heapify
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = []
        vis = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

        # Start with the top-left corner
        heapq.heappush(heap, (grid[0][0], 0, 0))
        vis.add((0, 0))

        while heap:
            cost, x, y = heapq.heappop(heap)
            
            # Early exit condition
            if (x, y) == (n - 1, n - 1):
                return cost
            
            # Explore four possible directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in vis:
                    heapq.heappush(heap, (max(grid[nx][ny], cost), nx, ny))
                    vis.add((nx, ny))  # Mark as visited when adding to the heap

        return -1
            

            


         
        


        