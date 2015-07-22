class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        
        jumps = 0
        count = len(nums) -1
        #base cases
        if count == 0:
            return 0
        elif nums[0] >= count:
            return 1
        else:
            curr = 0
            maxd = 0
            for i in range(len(nums)):
                if i > maxd:
                    maxd = curr
                    jumps += 1
                curr = max(curr,i+nums[i])
            return jumps