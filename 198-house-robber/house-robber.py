class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])
        
        dp = [0] * (n+1)
        dp[0], dp[1], dp[2] = 0, nums[0], nums[1]

        for i in range(3, n+1):
            dp[i] = nums[i-1] + max(dp[i-2], dp[i-3])

        return max(dp[-1], dp[-2])