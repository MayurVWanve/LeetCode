class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_list, min_list = [nums[0]],[nums[0]]
        for i in range(1, len(nums)):
            max_list.append(max(nums[i], nums[i]*max_list[i-1],nums[i]*min_list[i-1]))
            min_list.append(min(nums[i], nums[i]*max_list[i-1],nums[i]*min_list[i-1]))
        
        # print(max_list, min_list)
        return max(max_list)
        