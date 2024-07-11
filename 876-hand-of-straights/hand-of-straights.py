# class Solution:
#     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
#         n = len(hand)
#         if n % groupSize != 0:
#             return False

#         hand.sort() # Complexity bumps to O(nlogn)

#         soln = [[] for i in range(n//groupSize)]

#         for i in hand:
#             flag = False
#             for group in soln:
#                 if len(group) == 0 or (len(group) < groupSize and (group[-1] +1 ) == i):
#                     group.append(i)
#                     flag = True
#                     break
            
#             if flag == False:
#                 return False        
#         return True

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
        
        if groupSize == 1:
            return True

        h = hand.copy()
        heapq.heapify(h)

        Map = Counter(hand)

        while Map:

            start = -1
            while h and start not in Map:
                start = heapq.heappop(h)
            if not h:
                return False
            
            for value in range(start, start+groupSize):
                if value in Map:
                    if Map[value] == 1:
                        Map.pop(value)
                    else:
                        Map[value] -= 1
                else:
                    return False

        return True
                
        