class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapq.heapify(nums)

        while len(nums) > 1:
            num1, num2 = heapq.heappop(nums), heapq.heappop(nums)
            if num1 >= k:
                return count
            heapq.heappush(nums, ((num1 * 2) + num2))
            count+=1

        return count
        