# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return True if not subRoot else False
        
        if root and not subRoot:
            return True
        
        def isSameTree(p, q):
            if not p and not q:
                return True
            
            if not p and q or not q and p:
                return False
            
            return True if p.val == q.val and isSameTree(p.left,q.left) and isSameTree(p.right,q.right) else False


        return isSameTree(root, subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)

        


        