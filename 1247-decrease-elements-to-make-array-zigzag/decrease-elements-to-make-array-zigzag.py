class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        target1, target2,nums_copy = 0,0, nums.copy()

        #case 1 : >,< ...
        for i in range(len(nums)-1,0,-1):
            if i%2 == 1 and nums[i-1] <= nums[i]:
                temp = nums[i] - nums[i-1] +1
                target1+=temp
                nums[i] -= temp
            
            if i%2 == 0 and nums[i-1] >= nums[i]:
                temp = nums[i-1] - nums[i] + 1
                target1+=temp
                nums[i-1] -=temp
            
        
        # Case 2: <,>...:
        nums = nums_copy

        for i in range(len(nums)-1,0,-1):
            if i%2 == 1 and nums[i-1] >= nums[i]:
                temp = nums[i-1] - nums[i] +1
                target2+=temp
                nums[i-1]-=temp
            
            if i%2 == 0 and nums[i-1] <= nums[i]:
                temp = nums[i] - nums[i-1] + 1
                target2+=temp
                nums[i] -= temp
                # print(temp, target2, nums[i-1], nums[i])
        
        # print(target1, target2)
        return min(target1, target2)