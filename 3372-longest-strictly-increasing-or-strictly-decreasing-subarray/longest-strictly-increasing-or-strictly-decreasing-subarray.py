from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        window, i = 1, 0  
        flag = 0  # 0: uninitialized, 1: increasing, -1: decreasing
        
        for j in range(1, n):
            if nums[j] > nums[j - 1]:  #increasing
                if flag == -1: # decreasing
                    i = j - 1 
                flag = 1
            elif nums[j] < nums[j - 1]:  
                if flag == 1:  
                    i = j - 1  
                flag = -1
            else: 
                flag = 0
                i = j
            
            window = max(window, j - i + 1)  
        
        return window
