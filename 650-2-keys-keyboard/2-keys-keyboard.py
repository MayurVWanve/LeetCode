class Solution:
    def minSteps(self, n: int) -> int:
        keys, soln  = n, 0 
        while keys != 1:
            for i in range(2,keys+1):
                if keys % i == 0:
                    soln += i
                    keys = keys//i 
                    break
        return soln 


        