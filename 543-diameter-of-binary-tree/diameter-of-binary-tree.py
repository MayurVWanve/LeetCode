# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = 0

        def maxLen(node):
            nonlocal maxD

            if not node:
                return 0
            
            else:
                l, r = maxLen(node.left), maxLen(node.right)
                maxD = max(maxD,l+r)
                return 1 + max(l,r)
        
        if not root:
            return 0
        
        diameter = maxLen(root.left) + maxLen(root.right)
        return max(maxD, diameter)


        