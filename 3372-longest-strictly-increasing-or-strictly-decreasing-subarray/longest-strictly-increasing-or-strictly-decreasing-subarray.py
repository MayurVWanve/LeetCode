from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        window, i = 1, 0  # Initialize window to at least 1
        flag = 0  # 0: uninitialized, 1: increasing, -1: decreasing
        
        for j in range(1, n):
            if nums[j] > nums[j - 1]:  # Increasing sequence
                if flag == -1:  # Previously decreasing
                    i = j - 1  # Reset start of new subarray
                flag = 1
            elif nums[j] < nums[j - 1]:  # Decreasing sequence
                if flag == 1:  # Previously increasing
                    i = j - 1  # Reset start of new subarray
                flag = -1
            else:  # Same value, reset
                flag = 0
                i = j
            
            window = max(window, j - i + 1)  # Update longest window
        
        return window
