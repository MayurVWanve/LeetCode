class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left, right, soln, curr = [0] * n,[0] * n,[0] * n, 0

        for i in range(len(boxes)):
            if i == 0:
                left[i] = curr
            else:
                left[i] = left[i-1] + curr
                
            curr += 1 if boxes[i] == '1' else 0
        
        # print(f'Left: {left}')

        curr = 1 if boxes[n-1] == '1' else 0
            
        for i in range(len(boxes)-2, -1, -1):

            right[i] = right[i+1] + curr
            curr += 1 if boxes[i] == '1' else 0

        # print(f'Right: {right}')

        for i in range(n):
            soln[i] = left[i] + right[i]


        return soln


        