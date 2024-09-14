class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_ele, count, max_count, i = max(nums), 0, 0, 0
        # print(max_ele)
        while i < len(nums):
            if nums[i] == max_ele:
                while i+1 < len(nums) and nums[i] == nums[i+1]:
                    count+=1
                    i+=1
                max_count = max(max_count, count)
                count = 0
                i+=1
            
            else:
                i+=1

        return 1 + max_count

            

        