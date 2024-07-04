class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nums = [((points[i][0]*points[i][0]) + (points[i][1]* points[i][1]), points[i]) for i in range(len(points))]
        heapq.heapify(nums)
        # print(nums)
        nums = heapq.nsmallest(k, nums)
        # ans = [num[1] for num in nums]
        return [num[1] for num in nums]


        
        