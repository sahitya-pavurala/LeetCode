# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, number):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if root is None:
            return False
        
        stack = [(root,[])]
        
        while stack != []:
            node, tmplist = stack.pop()
            new_value = sum(tmplist) + node.val
            tmplist = tmplist + [node.val]
            
            if new_value == number and node.left is None and node.right is None:
                return True
            
            if node.left:
                stack.append((node.left,tmplist))
            if node.right:
                stack.append((node.right,tmplist))
            
        return False
        