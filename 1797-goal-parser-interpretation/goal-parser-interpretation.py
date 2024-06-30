class Solution:
    def interpret(self, command: str) -> str:
        soln, i = [], 0

        while i<len(command):
            if command[i] == 'G':
                soln.append('G')
                i+=1
            
            elif command[i] == '(' and command[i+1] == ')':
                soln.append('o')
                i+=2
            
            else:
                soln.append('al')
                i+=4
            
        
        return ''.join(soln)
        