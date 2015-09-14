class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
            
        elif x < 10:
            return True
            
        result = 0
        pre = x
        while x != 0:
            
            y = x%10
            x = x/10
            result = 10*result + y
        
        print result
        if result == pre:
            return True
        
        return False


obj = Solution()
print obj.isPalindrome(11)