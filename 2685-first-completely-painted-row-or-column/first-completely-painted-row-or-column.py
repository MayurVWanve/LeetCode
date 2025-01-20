class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        lookup = defaultdict(int)
        table = {}

        for i in range(m):
            for j in range(n):
                table[mat[i][j]] = (i,j)

        for pos, ele in enumerate(arr):
            r,c = table[ele]
            lookup[(0,r)] +=1
            lookup[(1,c)] +=1 
            if lookup[(0,r)] == n or lookup[(1,c)] == m:
                return pos
        