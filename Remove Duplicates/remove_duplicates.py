class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 
        count = 1
        pre = nums[0]
        end = len(nums)
        for i in range(1,end):
            
            if pre != nums[i]:
                nums[count] = nums[i]
                count +=1
                
            pre = nums[i]
            
            
        
        return count
        