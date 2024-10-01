from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count, ans = Counter(nums), -1
        for key, value in count.items():
            if value == 1:
                ans = max(key, ans)
        
        return ans
        