class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count = 0

        while num2 > 0:
            num2 = num2 & (num2 - 1)
            count+=1
        
        soln = 0
        for i in range(31, -1, -1):
            if count > 0 and (num1 & 1<<i) > 0:
                soln |= (1<<i)
                count-=1

        
        for i in range(31):
            if count > 0 and (soln & 1<<i) == 0:
                soln |= (1<<i)
                count-=1
        

        return soln

       
                                             
        
