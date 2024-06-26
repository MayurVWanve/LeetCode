class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        soln, curr = [], ['(']

        def helper(curr, pos , neg , tot):
            if len(curr) == 2*n and tot == 0:
                soln.append(''.join(curr))
                return
            
            if pos > n or neg > n or tot < 0:
                return 

            curr.append('(')
            helper(curr, pos +1, neg, tot +1)
            curr.pop()

            curr.append(')')
            helper(curr, pos , neg + 1, tot -1)
            curr.pop()
            
        
            
        helper(curr, 1, 0 , 1)
        return soln