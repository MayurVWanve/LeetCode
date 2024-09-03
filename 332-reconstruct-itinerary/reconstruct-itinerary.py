class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Every edge has to be visited: Topological Sort -> Sort the soln set someway
        # If we have a choice initially, visit the lexicographically smaller airport.
        # n, graph, soln = len(tickets), defaultdict(list), ["JFK"]
        # # tickets.sort()

        # for src, des in tickets:
        #     graph[src].append(des)

        # for key,val in graph.items():
        #     graph[key].sort()

        # # print(f'Sorted graph: {graph}')

        # def dfs(src, edges):
        #     nonlocal soln
        #     if edges == 0:
        #         return True
            
        #     if not graph[src]:
        #         return False
            
        #     dest = graph[src].copy()
        #     for des in dest:
        #         # print(f'Destination visiting : {des}')
        #         soln.append(des)
        #         graph[src].remove(des)
        #         if dfs(des, edges-1):
        #             return True
        #         # print(f'{des} not feasible. Edges : {edges}')
        #         soln.pop()
        #         graph[src].append(des)
        #         # print(f'Graph: {graph}, soln : {soln}')



        # dfs('JFK', n)
        # return soln

        graph = defaultdict(list)

        # Construct the graph
        for src, dest in tickets:
            graph[src].append(dest)

        # Sort destinations lexicographically
        for src in graph:
            graph[src].sort(reverse=True)

         # Return reversed solution to get the right order

        def dfs(src, graph, soln):
            while graph[src]:
                next_dest = graph[src].pop()  # Take the next destination
                dfs(next_dest, graph, soln)
            soln.append(src)

        soln = []
        dfs('JFK', graph, soln)
        return soln[::-1] 





        