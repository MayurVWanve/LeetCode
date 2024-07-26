class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        visited ,n  = set(), len(triplets)

        t1, t2, t3 = target[0], target[1], target[2]
        for i in range(n):
            a,b,c = triplets[i][0], triplets[i][1], triplets[i][2]
            if (a<=t1 and b<=t2 and c<=t3):
                if a == t1 and 0 not in visited:
                    visited.add(0)
                if b == t2 and 1 not in visited:
                    visited.add(1)
                if c == t3 and 2 not in visited:
                    visited.add(2)
            
        return True if len(visited) == 3 else False
        