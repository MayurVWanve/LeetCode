class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort(reverse = True)
        return min((nums[0] - nums[-4]),(nums[1]- nums[-3]),(nums[2]- nums[-2]),(nums[3]- nums[-1]))

        