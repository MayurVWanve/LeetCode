class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, res, n = [], 0, len(heights)
        for pos, ele in enumerate(heights):
            if not stack or ele > stack[-1][1]:
                stack.append((pos, ele))
            elif ele == stack[-1][1]:
                continue
            else:
                while stack and stack[-1][1] > ele:
                    prev_pos, prev_ele = stack.pop()
                    res = max(res, prev_ele * (pos - prev_pos))
                stack.append((prev_pos,ele))
        

        while stack:
            pos, ele = stack.pop()
            res = max(res, ele * (n-pos))
        
        return res


        
                

        