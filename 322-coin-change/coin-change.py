class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0 

        bag = [float('inf')] * (amount+1)
        bag[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0 :
                    bag[i] = min(bag[i], 1 + bag[i - coin])


        # print(bag)
        if bag[amount] != float('inf'):
            return bag[amount]
        else:
            return -1        