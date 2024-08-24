class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n, flag = len(board), len(board[0]),False

        def dfs(i,j,pos):
            nonlocal flag 
            if i < 0 or  j< 0 or i >= m or j >= n or board[i][j] != word[pos]:
                return 
            
            if pos == len(word)-1:
                if board[i][j] == word[pos]:
                    flag = True
                return 
            
            visited.add((i,j))

            # we are at correct char
            if (i+1,j) not in visited:
                visited.add((i+1,j))
                dfs(i+1,j, pos+1)
                visited.remove((i+1,j))

            if (i-1,j) not in visited:
                visited.add((i-1,j))
                dfs(i-1,j, pos+1)
                visited.remove((i-1,j))

            if (i,j+1) not in visited:
                visited.add((i,j+1))
                dfs(i,j+1, pos+1)
                visited.remove((i,j+1))

            if (i,j-1) not in visited:
                visited.add((i,j-1))
                dfs(i,j-1, pos+1)
                visited.remove((i,j-1))


        for i in range(m):
            for j in range(n):
                # if flag == True:
                #     return flag
                visited = set()
                if board[i][j] == word[0]:
                    dfs(i,j,0)
        

        return flag