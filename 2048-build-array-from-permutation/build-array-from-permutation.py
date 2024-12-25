class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        soln = []
        for i in range(len(nums)):
            soln.append(nums[nums[i]])
        
        return soln
        