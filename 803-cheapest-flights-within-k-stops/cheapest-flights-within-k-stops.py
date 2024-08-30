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

        distances = [float('inf')] * n
        distances[src] = 0

        # Temporary copy to keep track of updates in each iteration
        temp = distances[:]

        # Perform relaxations for at most k+1 edges
        for i in range(k + 1):
            # Copy the distances to start fresh for this round of edge relaxation
            temp = distances[:]
            updated = False  # Flag to check if any update was made in this iteration

            for sr, des, pri in flights:
                if distances[sr] != float('inf') and distances[sr] + pri < temp[des]:
                    temp[des] = distances[sr] + pri
                    updated = True  # An update was made

            # Update the distances array from the temporary array after all relaxations
            distances = temp
            # If no update was made, break early as no further updates will occur
            if not updated:
                break

        # Check if the destination is reachable
        return distances[dst] if distances[dst] != float('inf') else -1

                

            

        


        