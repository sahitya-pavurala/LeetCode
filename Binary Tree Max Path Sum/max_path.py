# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        self.max_val = -10 ** 10
        self.recurse_path(root)    
        
        return self.max_val
        
    def recurse_path(self,node):
        
        if node is None:
            return 0
        lmax = self.recurse_path(node.left)
        rmax = self.recurse_path(node.right)
        
        self.max_val = max(self.max_val,lmax+rmax+node.val)
        
        return max(node.val+max(lmax,rmax),0)
            
        
            
            
            
            
            