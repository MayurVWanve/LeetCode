class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numMap = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        soln, n  = [], len(digits)
        if n == 0:
            return soln
            
        def backtrack(i, curr):
            if i == n:
                soln.append(''.join(curr.copy()))
                return 
            
            for j in numMap[digits[i]]:
                curr.append(j)
                backtrack(i+1, curr)
                curr.pop()

        backtrack(0, [])
        return soln

         