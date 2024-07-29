# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        soln = []

        def dfs(node):

            if node.left:
                dfs(node.left)

            if len(soln) == k:
                return soln[-1]
            
            soln.append(node.val)

            if node.right:
                dfs(node.right)
            
            if len(soln) == k:
                return soln[-1]


        return dfs(root)
        

        
        