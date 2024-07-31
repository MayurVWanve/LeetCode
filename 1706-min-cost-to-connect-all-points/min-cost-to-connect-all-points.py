class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph, n, visit, q, tot = defaultdict(list), len(points), set(), [], 0
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                graph[(i,j)] = graph[(j,i)] = (abs(x1-x2) + abs(y1-y2))
            
        
        for i in range(1,n):
            q.append((graph[(0,i)], 0, i))
        
        heapq.heapify(q)
        visit.add(0)

        while len(visit) != n:
            cost, src, dest = heapq.heappop(q)
            if dest not in visit:
                tot += cost
                visit.add(dest)
                for i in range(n):
                    if i != dest:
                        heapq.heappush(q, (graph[(dest,i)], dest, i))

        return tot




