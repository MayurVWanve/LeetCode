class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        visited, q, timer, count = {}, deque(), 0, {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1
        
        heap = [-1 * value for key, value in count.items()]
        heapq.heapify(heap)

        while heap or q:
            # print(f'Iteration at time {timer}, heap:{heap}, q:{q} ')
            if heap:
                ele = heapq.heappop(heap)
                if ele+1 != 0:
                    q.append((ele+1, timer+n))
            
            if q and q[0][1] == timer:
                heapq.heappush(heap, q.popleft()[0])
            
            timer+=1
  
        return timer

        # print(visited, count)
        
