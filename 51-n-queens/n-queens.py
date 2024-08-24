class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        soln, temp, negD, cols, posD = [], [], set(), set(), set()
        print(temp)
        def findQueens(i, curr):
            # N-Queens are placed from row 0 : n-1 and n is successfully called.
            if i == n:
                t = '.' * n
                ans = [t[:i] + 'Q' + t[i+1:] for i in curr]
                soln.append(ans)
                return
            
            # We have to place a Queen on the ith row: options being col 0 : n-1
            for c in range(n):
                if (c not in cols) and (i+c not in posD) and (i-c not in negD):
                    curr.append(c)
                    cols.add(c)
                    negD.add(i-c)
                    posD.add(i+c)
                    findQueens(i+1, curr)
                    curr.pop()
                    cols.remove(c)
                    negD.remove(i-c)
                    posD.remove(i+c)

        findQueens(0, temp)
        return soln
        