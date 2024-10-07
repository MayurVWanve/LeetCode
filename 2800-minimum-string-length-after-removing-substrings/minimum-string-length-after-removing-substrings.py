class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for ele in s:
            if ele == 'B':
                if stack and stack[-1] == "A":
                    stack.pop()
                else:
                    stack.append(ele)
            elif ele == 'D':
                if stack and stack[-1] == "C":
                    stack.pop()
                else:
                    stack.append(ele)           
            else:
                stack.append(ele)

        return len(stack)