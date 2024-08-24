class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, pos):
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[pos] or (i,j) in visited:
                return False
            
            if pos == len(word) - 1 and board[i][j] == word[pos]:
                return True  # Found the word
            
            # Temporarily mark the cell as visited by changing its value
            # temp, board[i][j] = board[i][j], '#'
            visited.add((i,j))
            # Explore all four directions
            found = (dfs(i+1, j, pos+1) or
                     dfs(i-1, j, pos+1) or
                     dfs(i, j+1, pos+1) or
                     dfs(i, j-1, pos+1))
            
            # Restore the cell's original value
            visited.remove((i,j))
            
            return found

        for i in range(m):
            for j in range(n):
                visited = set()
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True  # If found, return True immediately
        
        return False