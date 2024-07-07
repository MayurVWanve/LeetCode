class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        new, rem,  ans = numBottles, 0, 0

        while new!=0:
            # print(f'Before: {ans, rem ,new}')
            ans+=new
            rem += new % numExchange
            new = new // numExchange
            new += rem//numExchange
            rem = rem % numExchange
            # print(f'After: {ans, rem ,new}')
        
        return ans
        