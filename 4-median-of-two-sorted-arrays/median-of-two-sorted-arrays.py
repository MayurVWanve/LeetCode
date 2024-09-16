from heapq import heappop, heappush
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        maxheap, minheap = [],[]    
        nums1+=nums2
        for ele in nums1:
            heappush(maxheap,(-1*ele))
            if (minheap and (-1 * maxheap[0]) > minheap[0]) or len(maxheap) > len(minheap)+1:
                e = -1 * heappop(maxheap)
                heappush(minheap, e)
            if len(maxheap) + 1 < len(minheap):
                heappush(maxheap, (-1*heappop(minheap)))
        
        if len(maxheap) > len(minheap):
            return (-1 * maxheap[0])
        
        if len(maxheap) < len(minheap):
            return minheap[0]
        
        return ((-1 * maxheap[0]) + minheap[0]) / 2