class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        m1, m2 = 0, 0

        y2diff, y1diff, x2diff, x1diff = (points[2][1] - points[1][1]),(points[1][1] - points[0][1]), (points[2][0] - points[1][0]),(points[1][0] - points[0][0])

        if y2diff == 0 and x2diff == 0 or y1diff == 0 and x1diff == 0 or x2diff == 0 and x1diff == 0:
            return False
        
        if x2diff == 0 or x1diff == 0:
            return True

        m2 = y2diff / x2diff
        m1 = y1diff / x1diff
        # print(m1,m2)

        return True if m1!=m2 else False
        