class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack , n, m = [], len(s), len(part)
        part = list(part)

        for i in range(n):
            if s[i] == part[-1]:
                k = len(stack)
                # print(f'1:{stack[k-m+1:]} 2: {part[:-1]}')
                if (k >= m-1) and (stack[k-m+1:] == part[:-1]):
                    for j in range(m-1):
                        stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

            # print(stack)
        

        return ''.join(stack)