class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        check = {}
        for key in range(0,len(nums)):
            if check.has_key(target-nums[key]):
                return check[target-nums[key]]+1,key+1
            
            check[nums[key]] = key 