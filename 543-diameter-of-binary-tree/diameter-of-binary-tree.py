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
            if not node:
                return 0
            
            else:
                return 1 + max(maxLen(node.left), maxLen(node.right))
        
        if not root:
            return 0
        
        diameter = maxLen(root.left) + maxLen(root.right)
        diameterLeft = self.diameterOfBinaryTree(root.left)
        diameterRight = self.diameterOfBinaryTree(root.right)
        return max(diameterLeft, diameter,diameterRight)


        