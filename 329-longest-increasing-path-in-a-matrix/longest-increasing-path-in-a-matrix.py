class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n, cache, soln = len(matrix), len(matrix[0]), {}, 0

        def dp(i,j):
            
            nonlocal soln

            if i >= m or j >= n or i<0 or j<0:
                return 0

            if (i,j) in cache:
                return cache[(i,j)]

            a,b,c,d = 0,0,0,0 

            if i>-0 and matrix[i][j] < matrix[i-1][j]:
                a = 1 + dp(i-1,j)
            
            if i<m-1 and matrix[i][j] < matrix[i+1][j]:
                b = 1 + dp(i+1,j)

            if j < n-1 and matrix[i][j] < matrix[i][j+1]:
                c = 1 + dp(i,j+1)

            if j > 0 and matrix[i][j] < matrix[i][j-1]:
                d = 1 + dp(i,j-1)
            
            cache[(i,j)] = max(a,b,c,d)
            
            soln = max(soln, cache[(i,j)])
            return cache[(i,j)]


            
        for i in range(m):
            for j in range(n):
                if (i,j) not in cache:
                    cache[(i,j)] = dp(i,j)

        print(cache)
        return soln+1
        