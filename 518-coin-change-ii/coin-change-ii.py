# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         dp, n = {}, len(coins)

#         def dfs(curr, pos):
#             if pos >= n or curr > amount:
#                 return 0

#             if curr == amount:
#                 dp[(curr, pos)] = 1
#                 return 1

#             if (curr,pos) in dp:
#                 return dp[(curr,pos)]

#             # dp[(curr,i)] = dfs(curr+ coins[i], i) + dfs(curr+ coins[i], i+1)
#             temp = 0
#             for i in range(pos, n):
#                 temp += dfs(curr+coins[i], i)

#             dp[(curr,i)] = temp
#             return dp[(curr,i)]
            
#         ans = dfs(0, 0)
#         print(dp)
#         return ans
#         #return dfs(0, 0)
        
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(n+1)]

        #Last col all 1 
        for i in range(n+1):
            dp[i][amount] = 1


        for i in range(n-1, -1, -1):
            for j in range(amount-1, -1, -1):
                # print(f"{i},{j}: {amount-j-coins[i]}, {dp[i+1][j]}, {dp[i][amount-j-coins[i]]}")
                dp[i][j] = dp[i+1][j] if amount-j-coins[i] < 0 else dp[i+1][j] + dp[i][j+coins[i]]

        # print(dp)
        return dp[0][0]     