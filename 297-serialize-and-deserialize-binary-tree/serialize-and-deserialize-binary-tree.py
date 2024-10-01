# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []
        def traverse(node):
            if not node:
                data.append('N')
                return 
            
            data.append(str(node.val))
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        data = ','.join(data)
        return data

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = list(data.split(','))

        # print(f'Decoded data: {data}, type: {type(data)}')
        def construct(itr):
            # print(f"Current position: {pos}, value: {data[pos]}")  # Debug print
            val = next(itr)
            if val == 'N':
                # print(f"Returning None for position: {pos}")  # Debug print
                return None
            
            
            

            node = TreeNode(int(val))

            # print(f"Created TreeNode with value: {node.val} at position: {pos}")  # Debug print

            node.left = construct(itr)
            node.right = construct(itr)
            # print(f"TreeNode with value: {node.val} has left child {node.left} and right child {node.right}")  # Debug print
            return node

        if len(data) == 1:
            return None
        root = construct(iter(data))
        # print(f"Root: {root.val}")  # Debug print
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))