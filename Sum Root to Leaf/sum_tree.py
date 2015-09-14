# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
        
        result =[]
        stack = []
        stack.append((root,[]))
        while stack != []:
            node, tmplst = stack.pop()
            tmplst = tmplst + [str(node.val)]
            if node.left is None and node.right is None:
                result.append(tmplst)
                
            if node.right:
                stack.append((node.right,tmplst))
            if node.left:
                stack.append((node.left,tmplst))
        
        final_val = 0
        for lst in result:
            final_val += int("".join(lst))
        
        return final_val
        
        