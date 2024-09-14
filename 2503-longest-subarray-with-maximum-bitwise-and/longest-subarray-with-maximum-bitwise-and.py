class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_ele, temp, soln = max(nums), 0,0

        for i in range(len(nums)):
            if nums[i] == max_ele:
                temp+=1
            else:
                soln = max(soln,temp)
                temp = 0

        return max(soln,temp)


            

        