class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n, soln, curr = len(s), [], []

        def isPalin(a):
            if a == a[::-1]:
                return True
            else:
                return False

        def findPartitions(index, curr):
            if index == n:
                soln.append(curr.copy())
                return 
            
            if index > n:
                return 

            for i in range(index, n):
                if isPalin(s[index:i+1]):
                    curr.append("".join(s[index:i+1]))
                    findPartitions(i+1, curr)
                    curr.pop()
            return 

        findPartitions(0,curr)
        return soln
        