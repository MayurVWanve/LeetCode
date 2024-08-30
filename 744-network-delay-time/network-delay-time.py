from heapq import heapify, heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap, graph, vis = [], defaultdict(list), {k}
        dist = {i+1:float('inf') for i in range(n)}
        dist[k] = 0
        for src, dst, time in times:
            graph[src].append((dst, time))
        
        for dst, time in graph[k]:
            minHeap.append((time, k, dst))
        
        heapify(minHeap)
        while minHeap:
            # print(f'Dist before the loop:{dist}, MinHeap:{minHeap}')
            time, src, dst = heappop(minHeap)
            if dist[dst] > dist[src] + time:
                dist[dst] = dist[src] + time
                vis.add(dst)
                for nei,new_time in graph[dst]:
                    heappush(minHeap,(new_time, dst, nei))
                # print(f'Dist after the loop:{dist}, vis:{vis}')
        maxtime = max(dist.values()) 
            
        return maxtime if maxtime != float('inf') else -1              

            
        
        
        

        