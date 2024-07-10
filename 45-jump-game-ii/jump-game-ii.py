class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        dp = [float('inf')] * n
        dp[n-1] = 0

        for i in range(n-2, -1, -1):
            temp = []
            for j in range(1, nums[i]+1):
                if i + j < n:
                    temp.append(1+dp[i+j])
            
            dp[i] = min(temp) if temp else float('inf')
        

        return dp[0]



        