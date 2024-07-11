class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack, temp = [], []
        for char in s:
            if char == ')':
                # print("In if loop", char)
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
                temp = []

            else:
                # print("In else loop", char)
                stack.append(char)
            
            print(stack)
        
        return ''.join(stack)
        