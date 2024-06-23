# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q, soln = deque(), []
        q.append((root,0))
        level, temp = 0, []

        if not root: 
            return soln
        
        while q:
            node = q.popleft()
            if node[1] != level:
                soln.append(temp)
                temp = []
                level+=1
            
            temp.append(node[0].val)
            if node[0].left:
                q.append((node[0].left, level+1))
            
            if node[0].right:
                q.append((node[0].right, level+1))

        soln.append(temp)
        return soln
            
                



        