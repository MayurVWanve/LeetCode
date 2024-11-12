class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        soln, lookup = [], set()
        def backtrack(val, curr):
            if len(curr) == n:
                res = int("".join(map(str, curr.copy())))
                if res not in lookup:
                    soln.append(res)
                    lookup.add(res)
                return 

            if val + k <=9:
                curr.append(val+k)
                backtrack(val+k, curr)
                curr.pop()
            
            if val - k >= 0:
                curr.append(val-k)
                backtrack(val-k, curr)
                curr.pop()


        for val in range(1,10):
            backtrack(val, [val])
        return soln
        