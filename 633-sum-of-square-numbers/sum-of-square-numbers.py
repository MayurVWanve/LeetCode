class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(math.sqrt(c))

        for i in range(n,-1,-1):
            # print("In loop")
            r = c - math.pow(i,2)
            r2 = math.sqrt(r)
            # print(r2, int(r2), r2 == int(r2))
            if r2 == int(r2):
                return True

        return False        