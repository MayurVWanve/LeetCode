class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_sum, lookup = -1, defaultdict(list)
        

        def helper(num):
            ele = 0
            while num > 0:
                ele += num%10
                num = num//10
            return ele

        for num in nums:
            ele = helper(num)
            if ele in lookup:
                if len(lookup[ele]) == 1:
                    tot = lookup[ele][0] + num
                    heapq.heappush(lookup[ele],num)
                    max_sum = max(max_sum, tot)

                else:
                    if lookup[ele][0] < num:
                        heapq.heappop(lookup[ele])
                        tot = lookup[ele][0] + num
                        heapq.heappush(lookup[ele],num)
                        max_sum = max(max_sum, tot)
                    else:
                        continue
                    
            else:
                heapq.heappush(lookup[ele],num)
        


        return max_sum
        