class Solution:
    def reverse(self, x: int) -> int:
        # Naive Solution:
        neg, res = False, 0

        if abs(x) > pow(2, 31):
            return 0

        if x < 0 :
            neg = True

        x = abs(x)
        while x:
            res = res*10 + (x%10)
            x = x//10
        
        if res > 2**31:
            return 0
            
        return -1 * res if neg else res
