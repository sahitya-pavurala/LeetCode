# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
            
        self.result = []
        self.stack = []
        node = root
        
        
        while node is not None or self.stack != []:
            if node != None:
                self.result.append(node.val)
                if node.right:
                    self.stack.append(node.right)
                node = node.left
                
            else:
                node = self.stack.pop()
                    

        return self.result
            
            
        
        
        # Using recursion
        # def recurse_tree1(node):
            
        #     if node == None:
        #         return
        #     else:
        #         self.result.append(node.val)
        #         recurse_tree(node.left)
        #         recurse_tree(node.right)
                
        # recurse_tree(root)
            
        return self.result
            
            
        