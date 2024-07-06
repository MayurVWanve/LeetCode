class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        direction, person = 0,0
        

        if time < n:
            return time + 1

        time-= (n-1)


        direction = time//(n-1)
        person = time%(n-1)

        return person + 1 if direction % 2==1 else (n - person)
