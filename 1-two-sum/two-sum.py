class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            if nums[i] in lookup:
                return [lookup[nums[i]], i]

            else:
                lookup[target - nums[i]] = i

        return -1