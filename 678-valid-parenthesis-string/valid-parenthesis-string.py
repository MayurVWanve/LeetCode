class Solution:
    def checkValidString(self, s: str) -> bool:
        stack, count = [], 0

        for i in s:
            if i == '(' or i == '*':
                stack.append(i)
            
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                elif stack and stack[-1] == '*':
                    temp = []
                    while stack and stack[-1] == '*':
                        temp.append(stack.pop())
                    
                    if stack:
                        stack.pop()
                        stack = stack + temp[:]
                    
                    else:
                        stack = stack + temp[:]
                        stack.pop()
                else:
                    return False
        
        for i in stack:
            if i == '(':
                count+=1
            else:
                count = max(0, count-1)
        

        return True if (len(stack) == 0 or count==0) else False
        


            
            
        