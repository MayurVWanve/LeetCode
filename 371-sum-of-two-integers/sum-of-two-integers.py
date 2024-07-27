class Solution:
    def getSum(self, a: int, b: int) -> int:
        # l = [a,b]
        # return sum(l)
        mask = 0xFFFFFFFF

        while (mask & b) != 0:
            t = a ^ b
            b = (a & b) << 1
            a = t

        return a if b == 0 else (mask & a)
        

        