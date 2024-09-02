class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # n , count, soln  = len(nums), {}, []

        # for ele in nums:
        #     if ele in count:
        #         count[ele] += 1
        #     else:
        #         count[ele] = 1

        # count_sorted = dict(sorted(count.items(), key = lambda x: x[1], reverse = True))

        # # print(count_sorted)

        # for key in count_sorted.keys():
        #     print(k)
        #     if k == 0:
        #         # print("In if",soln)
        #         return soln
        #     else:
        #         soln.append(key)
        #         # print("In else",soln)
        #         k-=1
        # return soln

        n, count, soln = len(nums), defaultdict(int), []
        for ele in nums:
            count[ele] += 1
        
        heap = [(-1 * val, key) for key, val in count.items()]
        heapq.heapify(heap)
        print(heap)

        for i in range(k):
            _, ele = heapq.heappop(heap)
            soln.append(ele)

        return soln

        
                