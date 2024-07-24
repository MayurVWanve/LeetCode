class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        i , j = 0, m - 1

        row, col = 0,0
        # Search for appropriate row
        # print("Searching Row")
        while i<=j:
            mid = (i+j)//2
            print(f'{i,j}:{mid}')

            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                row = mid
                break
            
            elif matrix[mid][0] > target:
                j = mid - 1 
            
            else:
                i = mid + 1

        # print(f'Row : {row}')

        # Search for appropriate column
        # print(f"n= {m, n}")
        i,j = 0, n - 1
        while i<=j:
            mid = (i+j)//2
            # print(f'{i,j}: Mid : {mid}')
            if matrix[row][mid] == target:
                return True
            
            if matrix[row][mid] < target:
                i = mid + 1
            
            else:
                j = mid - 1


        return False