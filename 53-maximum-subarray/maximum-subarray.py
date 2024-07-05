class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        soln = [0] * len(nums)
        soln[0] =nums[0]
        for i in range(1,len(nums)):
            soln[i] = max(nums[i] + soln[i-1], nums[i])
        return max(soln)
        