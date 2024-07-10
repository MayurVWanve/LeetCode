class Solution:
    def jump(self, nums: List[int]) -> int:
        # n = len(nums) DP -> O(n2)
        # if n == 1:
        #     return 0

        # dp = [float('inf')] * n
        # dp[n-1] = 0

        # for i in range(n-2, -1, -1):
        #     temp = []
        #     for j in range(1, nums[i]+1):
        #         if i + j < n:
        #             temp.append(1+dp[i+j])
            
        #     dp[i] = min(temp) if temp else float('inf')
        

        # return dp[0]

        # Greedy O(n)

        q, n = [(i+1,1) for i in range(nums[0])], len(nums)
        vis = set([i+1 for i in range(nums[0])])

        if n == 1:
            return 0

        while q:
            pos, dis = q.pop(0)
            if pos == n-1:
                return dis
            
            for i in range(1,nums[pos]+1):
                if pos + i not in vis:
                    vis.add(pos+i)
                    q.append((pos+i, 1 + dis))
        
        return -1


        
       



        