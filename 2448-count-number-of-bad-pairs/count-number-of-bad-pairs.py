class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        lookup, count, n  = defaultdict(int), 0, len(nums)

        total = (n * (n-1))//2

        for i in range(n):
            slope = nums[i] - i
            count+= lookup[slope]
            lookup[slope]+=1

        return total - count