from heapq import heappop, heappush, heapify
class Solution:
        def swimInWater(self, grid: List[List[int]]) -> int:
            n, heap, vis, directions = len(grid), [], set(), [(0, 1), (1, 0), (-1, 0), (0, -1)] # heap(cost, i, j) cost for that grid[i][j]

            heap.append((grid[0][0], 0,0))
            vis.add((0,0))

            while heap:
                # print(f'Heap : {heap}')
                cost, i, j = heappop(heap)
                vis.add((i,j))

                if (i,j) == (n-1,n-1):
                    return cost

                for dx, dy in directions:
                    i_new, j_new = i+dx, j+dy
                    # print(i_new, j_new)
                    if 0<=i_new<n and 0<=j_new<n and (i_new, j_new) not in vis:
                        heappush(heap,(max(grid[i_new][j_new],cost), i_new, j_new))
                        vis.add((i_new,j_new)) # Because of the fact that you're choosing a node with least cost, every time we add a node to our heap, we are sure that it is the least cost to reach there.

            return -1
            


         
        


        