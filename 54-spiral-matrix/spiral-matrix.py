class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        d, directions,vis, soln, m, n, c = 0, {0:[0,1], 1:[1,0], 2:[0, -1], 3:[-1,0]},{}, [], len(matrix),len(matrix[0]), 0
        i,j = 0,0

        while c != m*n:
            c+=1
            # print(i,j)
            soln.append(matrix[i][j])
            vis[(i,j)] = 1
            dr, dc = directions[d]
            next_i,next_j = i + dr, j + dc

            if (next_i,next_j) in vis or (next_i==0  and next_j == n) or (next_i== m and next_j==n-1) or (next_i==m-1 and next_j==-1):
                d = (d+1)%4
                dr, dc = directions[d]
                i,j = i + dr, j + dc


            else:
                i,j = next_i,next_j

        
        return soln



        
        