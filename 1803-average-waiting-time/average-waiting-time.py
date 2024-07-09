class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        soln, t = [], 0

        for x,y in customers:
            if x > t:
                soln.append(y)
                t = x+y
            else:
                soln.append(t+y-x)
                t += y
        
        return sum(soln)/ len(soln)
        