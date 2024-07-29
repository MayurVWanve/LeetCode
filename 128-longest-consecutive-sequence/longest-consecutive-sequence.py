class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        heapq.heapify(nums) #O(n)
        count, soln = 1, 1
        recent = heapq.heappop(nums)
        # print(f'First ele: {recent}, len(nums): {len(nums)}')

        for i in range(len(nums)):
            ele = heapq.heappop(nums)
            print(f'ele: {ele}')
            if ele == recent:
                continue
            elif ele  == recent+1:
                count+=1
                recent = ele
            else:
                count = 1 

            soln = max(soln,count)
            recent = ele

            # print(f'recent: {recent}, count : {count}, soln: {soln}' )
            

        return soln