# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        if root == None:
            return result

        def recurse(root,path):
            
            if root.left is None and root.right is None:
                result.append(path)
            if root.left:
                recurse(root.left,path + "->" + str(root.left.val))
            if root.right:
                recurse(root.right,path + "->" + str(root.right.val))
            
        recurse(root,str(root.val))
        
        return result
        
        
            
        