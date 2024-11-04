class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s1, g1 , matched, n, m, lookup = 0,0,0, len(goal), len(s), set()

        if m != n:
            return False

        for i in range(n):
            if goal[i] == s[0]:
                lookup.add(i)

        for pos in lookup:
            if s == goal[pos:] + goal[:pos]:
                return True

        
        return False