# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        result = []
        stack = []
        node  = root
        
        while node is not None or stack != []:
            
            if node is not None:
                result.append(node.val)
                if node.left:
                    stack.append(node.left)
                
                node = node.right
            else:
                node = stack.pop()
        
        
        # def recurse_tree(node):
            
        #     if node is None:
        #         return
            
            
        #     recurse_tree(node.left)
        #     recurse_tree(node.right)
        #     result.append(node.val)
            
        # recurse_tree(root)    
        return result[::-1]