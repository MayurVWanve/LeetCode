# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q, level, soln  = deque(), 0, []
        q.append((root,level))

        while q:
            node = q.popleft()

            if node[1] != level:
                soln.append(prev)
                level+=1
            
            if node[0].left:
                q.append((node[0].left, level +1))
            
            if node[0].right:
                q.append((node[0].right, level +1))
            
            prev = node[0].val

        soln.append(prev)

        return soln
        
        
        