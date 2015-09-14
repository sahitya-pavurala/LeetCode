class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ip1 = tuple(nums[:len(nums)-1])
        ip2 = tuple(nums[1:])
        
        
        if len(nums) > 1:
            first_sol = self.internal(ip1)
            second_sol = self.internal(ip2)
            return max(first_sol,second_sol)
        elif len(nums) == 1:
            return nums[0]
        else:
            return 0
            
    def internal(self,ip):
        check = {}
        check[()] = 0
        
        check[ip[0],] = ip[0]
    
        #last not included
        for i in range(1,len(ip)):
        
            temp_res = check[ip[:i-1]]
        
            if temp_res + ip[i] > check[ip[:i]]:
                check[ip[:i+1]] = temp_res + ip[i]
            else:
                check[ip[:i+1]] = check[ip[:i]]
        
        return check[ip]
        
        
            
        
        