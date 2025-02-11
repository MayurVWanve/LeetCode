class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for token in s:
            if '0' <= token <= '9':
                stack.pop()
            else:
                stack.append(token)
        

        return ''.join(stack)