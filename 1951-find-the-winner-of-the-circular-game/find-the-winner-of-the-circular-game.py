class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        soln, pos = [i+1 for i in range(n)], 0

        while len(soln) != 1:
            pos = ((pos + k)%len(soln)) -1 
            if pos < 0:
                pos+=len(soln)
            soln.pop(pos)
            # print(soln)

        return soln[0]
        