from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topological Sort Logic
        graph, indegree, q,visited  = defaultdict(list), [0 for i in range(numCourses)], deque(), {}

        for i, j in prerequisites:
            if i == j:
                return False
            graph[i].append(j)
            indegree[j] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                visited[i] = 1

        
        while(q):
            node = q.popleft()
            
            for i in graph[node]:
                indegree[i] -= 1
                
            for j in range(numCourses):
                if indegree[j] == 0 and j not in visited:
                    q.append(j)
                    visited[j] = 1

        
        return True if len(visited) == numCourses else False

        # n, graph, vis = len(numCourses), defaultdict(list), set()

        # for i, j in prerequisites:
        #     if i == j:
        #         return False
        #     graph[i].append(j)


            





        


         


        
        


        