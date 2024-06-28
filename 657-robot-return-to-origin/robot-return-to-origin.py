class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h, v = 0,0

        for i in moves:
            if i == "U":
                v+=1

            elif i == "D":
                v-=1
            
            elif i == "L":
                h-=1
            else:
                h+=1

        return True if h==0 and v==0 else False

