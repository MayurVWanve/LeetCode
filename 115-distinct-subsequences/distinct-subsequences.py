class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m , cache = len(s),len(t) , {}

        def dp(i,j):
            if j == m:
                return 1
            
            if (i == n and j!=m) or (m-j) > (n-i):
                return 0

            if (i,j) in cache:
                return cache[(i,j)]

            if s[i] == t[j]:
                cache[(i,j)] = dp(i+1, j+1) + dp(i+1, j)
            
            else:
                cache[(i,j)]  = dp(i+1, j)

            return cache[(i,j)] 

        return dp(0,0)
        