# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        ptr1 = head
        ptr2 = head
        pre = head
        
        if head.next == None:
            return []
        
        for i in range(n):
            ptr2 = ptr2.next;
        
        if ptr2 == None:
            head = head.next
            return head
        while ptr2 != None:
            pre = ptr1
            ptr1 = ptr1.next
            ptr2= ptr2.next
        
    
        pre.next = ptr1.next
        
        return head
        
        