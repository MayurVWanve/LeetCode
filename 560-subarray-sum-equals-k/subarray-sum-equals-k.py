class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Use the prefix Sum approach -> Instead of what we want in the current window, Think of what prefix can we reomove from 
        # current window so that we get the required sum k. Keep adding the freqwncy of prefix sum in a hash map

        prefix = defaultdict(int)
        prefix[0], curr, soln = 1, 0, 0

        for i in range(len(nums)):
            curr += nums[i]
            if curr - k in prefix:
                soln+=prefix[(curr-k)]
            prefix[curr]+=1

        return soln
        

        