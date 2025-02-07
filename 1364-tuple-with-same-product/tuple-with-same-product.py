class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # lookup, soln, n = set(), 0, len(nums)
        # nums.sort()

        # def search(temp):
        #     nonlocal soln
        #     res = temp[0] * temp[-1]
        #     i,j = 1, len(temp)-2
        #     while i<j:
        #         if temp[i] * temp[j] == res:
        #             soln+=1
        #             i+=1
        #             j-=1
                
        #         elif temp[i] * temp[j] < res:
        #             i+=1
                
        #         else:
        #             j-=1

        #     return 0
                


        # def helper(temp):
        #     if len(temp) < 4:
        #         return 0
        #     if (temp[0], temp[-1]) not in lookup :
        #         lookup.add((temp[0], temp[-1]))
        #         search(temp)
        #         helper(temp[1:])
        #         helper(temp[:-1])

        # helper(nums)
        # return soln*8

        lookup, soln  = defaultdict(int), 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                lookup[nums[i] * nums[j]] +=1
        
        for val in lookup.values():
            if val > 1:
                soln += ((val * (val-1))//2)
        
        return soln * 8

        