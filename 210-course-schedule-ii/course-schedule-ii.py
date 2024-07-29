class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological Sort Logic
        # graph, indegree, q,visited, soln   = defaultdict(list), [0 for i in range(numCourses)], deque(), {}, []

        # for i, j in prerequisites:
        #     if i == j:
        #         return False
        #     graph[j].append(i)
        #     indegree[i] += 1
        
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         q.append(i)
        #         visited[i] = 1

        
        # while(q):
        #     node = q.popleft()
        #     soln.append(node)
            
        #     for i in graph[node]:
        #         indegree[i] -= 1
                
        #     for j in range(numCourses):
        #         if indegree[j] == 0 and j not in visited:
        #             q.append(j)
        #             visited[j] = 1

        
        # return soln if len(visited) == numCourses else []

        graph, vis, soln, finish = defaultdict(list), set(), [], set()

        for i, j in prerequisites:
            if i == j:
                return False
            graph[j].append(i)

        
        def dfs(node):
            print(f'Node Considered: {node}')
            nonlocal soln

            if node in finish:
                return True
            
            if node in vis:
                return False

            vis.add(node)

            for neigh in graph[node]:
                print(f'Node and neighbour: {node, neigh}')
                if not dfs(neigh):
                    return False
                
            
            vis.remove(node)
            finish.add(node)
            soln.append(node)
            return True
            
        
        for i in range(numCourses):
            if i not in finish:
                if not dfs(i):
                    return []
        
        return soln[::-1]



