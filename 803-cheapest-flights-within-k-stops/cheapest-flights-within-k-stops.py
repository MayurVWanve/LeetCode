class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # KRUSKAL's Soln: Not Efficient -> k stops -> Bellman Ford Approach
        # graph, n, fcost, visit, q  = defaultdict(list), len(flights), float('inf'), set(), []

        # for s, d, c in flights:
        #     graph[s].append([d, c])

        # for d, c in graph[src]:
        #     q.append([c, src, d,0])
        
        # visit.add(src)
        # heapq.heapify(q)

        # while q:
        #     c,s,d, st = heapq.heappop(q)
            
        #     if d == dst and st<=k:
        #         return c
            
        #     if st < k:
        #         for nei, cost in graph[d]:
        #             heapq.heappush(q, ([c + cost ,d, nei,st+1]))
        

        # return -1

        soln = {i: float('inf') for i in range(n)}
        soln[src] = 0
        temp = soln.copy()
        # print(soln)

        for i in range(k+1):
            # print(f'Soln before update: {soln}')
            # print(f'Temp before update: {temp}')
            temp = soln.copy()
            flag = False
            for sr, des, pri in flights:
                if soln[sr]!= float('inf') and soln[sr] + pri < temp[des]:
                    # print(f'New Path Found {des} : {soln[sr]} + {pri}')
                    temp[des] = soln[sr] + pri
                    flag = True

            soln = temp.copy()
            if not flag:
                break

            # print(f'Soln after update: {soln}')
            # print(f'Temp after update: {temp}')
        
        return soln[dst] if soln[dst] != float('inf') else -1

                

            

        


        