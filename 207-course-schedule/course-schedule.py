from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, indegree, q,visited  = defaultdict(list), [0 for i in range(numCourses)], [], {}

        for i, j in prerequisites:
            graph[j].append(i)
            indegree[i] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                visited[i] = 1

        
        while(q):
            node = q.pop(0)
            
            for i in graph[node]:
                indegree[i] -= 1
                
            for j in range(numCourses):
                if indegree[j] == 0 and j not in visited:
                    q.append(j)
                    visited[j] = 1

        
        return True if len(visited) == numCourses else False


        


         


        
        


        