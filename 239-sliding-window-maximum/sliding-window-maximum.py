class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n, lookup, maxHeap,i,j,soln = len(nums), defaultdict(int), [],0,0,[]

        while k!=0:
            lookup[nums[j]]+=1
            maxHeap.append((-1 * nums[j]))
            k-=1
            j+=1
        heapq.heapify(maxHeap)
        soln.append(-1 * maxHeap[0])
        
        while j<n:
            # print("Lookup before loop :", lookup)
            if lookup[nums[i]] == 1:
                del(lookup[nums[i]])
            else:
                lookup[nums[i]] -= 1
            i+=1
            lookup[nums[j]] += 1
            heapq.heappush(maxHeap, -1*nums[j])
            j+=1
            # print(f'Lookup: {lookup}, Maxheap: {maxHeap}')

            while (-1 * maxHeap[0]) not in lookup:
                heapq.heappop(maxHeap)
            soln.append(-1 * maxHeap[0])
            # print(soln)
            

        return soln