class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological Sort Logic
        graph, indegree, q,visited, soln   = defaultdict(list), [0 for i in range(numCourses)], deque(), {}, []

        for i, j in prerequisites:
            if i == j:
                return False
            graph[j].append(i)
            indegree[i] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                visited[i] = 1

        
        while(q):
            node = q.popleft()
            soln.append(node)
            
            for i in graph[node]:
                indegree[i] -= 1
                
            for j in range(numCourses):
                if indegree[j] == 0 and j not in visited:
                    q.append(j)
                    visited[j] = 1

        
        return soln if len(visited) == numCourses else []