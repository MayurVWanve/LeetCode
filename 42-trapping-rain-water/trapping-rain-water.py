class Solution:
    def trap(self, height: List[int]) -> int:
        n, maxLeft, maxRight,left, right, area = len(height), [], [], height[0], height[-1], 0

        for i in range(n):
            if height[i]>left:
                maxLeft.append(height[i])
                left = height[i]
            else:
                maxLeft.append(left)

        for i in range(n-1, -1,-1):
            if height[i]>right:
                maxRight.append(height[i])
                right = height[i]
            else:
                maxRight.append(right)
        
        maxRight = maxRight[::-1]

        for i in range(n):
            temp = min(maxRight[i], maxLeft[i]) - height[i]
            if temp > 0:
                area+= temp
        
        return area


        

        

        