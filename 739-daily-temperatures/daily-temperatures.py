class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        soln, stack, pos = [0] * (n), [], 0
        # print(f'Tmap : {Tmap}')

        while pos < n:
            # print(f'pos : {pos}, stack: {stack}')
            if not stack or temperatures[pos] <= stack[-1][0]:
                stack.append((temperatures[pos], pos))

            else:
                while stack and temperatures[pos] > stack[-1][0]:
                    ele, p = stack.pop()
                    soln[p] = pos - p

                stack.append((temperatures[pos],pos))
            
            pos+=1
                
        return soln

        