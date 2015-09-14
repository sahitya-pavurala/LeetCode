# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, number):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        stack = []
        result = []
        if root is None:
            return result
        
        
        templist = []
        stack.append((root,templist))
    
        while len(stack) > 0:
            node,tmp = stack.pop()
            tempsum = node.val + sum(tmp)
            tmp = tmp + [node.val]
            if tempsum == number and node.left is None and node.right is None:
                result.append(tmp)
                
            if node.right:
                stack.append((node.right,tmp))
            if node.left:
                stack.append((node.left,tmp))
            
        return result