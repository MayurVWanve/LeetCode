class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # n = int(math.sqrt(c))

        # for i in range(n,-1,-1):
        #     # print("In loop")
        #     r = c - math.pow(i,2)
        #     r2 = math.sqrt(r)
        #     # print(r2, int(r2), r2 == int(r2))
        #     if r2 == int(r2):
        #         return True

        # return False 

        # Can Do it more efficiently with 2 pointers
        i,j = 0, int(math.sqrt(c))
        while i<=j:
            res = i*i + j*j
            if res == c:
                return True

            if res > c:
                j-=1

            else:
                i+=1

        return False       