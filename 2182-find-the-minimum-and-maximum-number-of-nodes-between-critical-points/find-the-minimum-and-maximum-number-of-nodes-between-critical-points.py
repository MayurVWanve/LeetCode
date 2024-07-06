# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        pos, points, soln = 1, [], [-1,-1]
        prev, curr = head, head.next

        if not curr.next:
            return soln

        while curr.next:
            nextN = curr.next
            if prev.val < curr.val and nextN.val < curr.val:
                points.append(pos)
            
            elif prev.val > curr.val and nextN.val > curr.val:
                points.append(pos)

            prev = curr
            curr = nextN
            pos+=1
        
        # print(f'Points: {points}')
        if len(points) > 1:
            minD = float('inf')
            for i in range(1, len(points)):
                minD = min(minD, points[i]- points[i-1])
            soln = [minD, points[-1]- points[0]]

        return soln




        