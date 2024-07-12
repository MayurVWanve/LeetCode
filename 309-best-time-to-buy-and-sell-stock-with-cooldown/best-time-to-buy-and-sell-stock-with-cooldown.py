class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, cache = True, {} #(target) Dp will cache what is the value of target in ith position

        def dp(pos, buy):

            if pos >= len(prices):
                # print(f'pos == {pos}')
                return 0

            if (pos,buy) in cache:
                # print(f'Cached Result: {pos, buy} : {cache[pos,buy]}')
                return cache[pos,buy]
            
            if buy: # We are allowed to buy
                # print("In Buy")
                cache[pos, buy] = max(dp(pos+1, False) - prices[pos], dp(pos+1, True))
            
            else: # We are allowed to sell
                # print("In else SELL")
                cache[pos, buy] = max(dp(pos+1, False), dp(pos + 2, True) + prices[pos])
                

            return cache[pos, buy]
        # print(cache)
        return dp(0,True)     