class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r,c,pac, atl = len(heights), len(heights[0]), set(), set()

        def dfs(i,j,prev,lookup):
            if i<0 or i>=r or j<0 or j>=c or heights[i][j]<prev or (i,j) in lookup:
                return 
            lookup.add((i,j))
            dfs(i-1,j,heights[i][j], lookup)
            dfs(i+1,j,heights[i][j], lookup)
            dfs(i,j-1,heights[i][j], lookup)
            dfs(i,j+1,heights[i][j], lookup)

            return 
        

        for i in range(r):
            dfs(i,0, heights[i][0], pac)
            dfs(i, c-1, heights[i][c-1], atl)
        
        for j in range(c):
            dfs(0,j,heights[0][j], pac)
            dfs(r-1,j, heights[r-1][j], atl)

        # print(f'PAcific:{pac}, Atlantic:{atl}')
        return pac.intersection(atl)

        

        
        

