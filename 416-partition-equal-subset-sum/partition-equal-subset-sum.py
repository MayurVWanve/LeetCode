class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 == 1:
            return False

        n, target, dp = len(nums), sum(nums)//2, {}

        def dfs(i, curr):
            if i >= n or curr > target:
                return False

            if (i, curr) in dp:
                return dp[(i, curr)]

            if curr == target:
                return True

            dp[(i, curr)] = dfs(i+1, curr) or dfs(i+1, curr + nums[i])

            return dp[(i, curr)]          

        return dfs(0,0)
        


        
        
        