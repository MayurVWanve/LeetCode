# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        def traverse(node):
            nonlocal maxSum

            if not node:
                return 0
            
            left, right  = 0, 0
            if node.left:
                left = traverse(node.left)
            
            if node.right:
                right = traverse(node.right)

            maxSum = max(maxSum, left + right + node.val, node.val, right + node.val, left + node.val)

            return node.val + max(0, left , right)

        soln = traverse(root)
        maxSum = max(maxSum, soln)
        return maxSum            

        traverse(root)
        return maxSum
        