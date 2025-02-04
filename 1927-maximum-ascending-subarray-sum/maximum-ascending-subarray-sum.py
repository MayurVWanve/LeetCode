class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n, curr, maxSum = len(nums), nums[0], nums[0]

        if n == 1:
            return maxSum
        
        for j in range(1, n):
            if nums[j] > nums[j-1]:
                curr+=nums[j]
            
            else:
                maxSum = max(maxSum, curr)
                curr = nums[j]


        return max(maxSum, curr)

        