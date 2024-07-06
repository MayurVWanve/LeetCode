class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        dist, k, ans = [], 0, []
        for i in range(len(s)):
            if s[i] == c:
                dist.append(i)

        for i in range(len(s)):
            # print("i, k, dist[k], dist[k-1] ",i, k, dist[k], dist[k-1])

            if i == dist[k]:
                # print(f'cond1')
                ans.append(abs(dist[k]-i))
                if k < (len(dist) - 1):
                    k+=1
            
            elif i > dist[k-1] and i < dist[k]:
                # print(f'cond2')
                ans.append(min(abs(dist[k-1]-i), abs(dist[k]-i)))
            
            else:
                # print(f'cond3')
                ans.append(abs(dist[k]-i))
        
        # print(f'dist: {dist}')

        return ans


        
                
        