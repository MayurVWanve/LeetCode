class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Cache: (CurrentSum, pos) -> Number of ways to get to target

        dp, n, ans = {}, len(nums), 0

        def dfs(pos, curr):
            nonlocal ans 

            if pos == n:
                return 0 if curr != target else 1

            if (pos, curr) in dp:
                return dp[(pos, curr)]
            
            dp[(pos, curr)] = dfs(pos+1, curr - nums[pos]) + dfs(pos+1, curr + nums[pos])
            return dp[(pos, curr)] 

        # print(dp)
        return dfs(0,0)