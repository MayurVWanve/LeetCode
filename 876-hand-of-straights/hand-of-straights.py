class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        hand.sort() # Complexity bumps to O(nlogn)
        
        soln = [[] for i in range(n//groupSize)]

        for i in hand:
            flag = False
            for group in soln:
                if len(group) == 0 or (len(group) < groupSize and (group[-1] +1 ) == i):
                    group.append(i)
                    flag = True
                    break
            
            if flag == False:
                return False        
        return True
                
        