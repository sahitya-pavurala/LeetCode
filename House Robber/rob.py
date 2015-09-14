def rob(nums):


	check = {}


	check[()] = 0
	check[(nums[0],)] = nums[0]

	for num in range(1,len(nums)):

		tempres = check[tuple(nums[:num-1])]

		if tempres + nums[num] > check[tuple(nums[:num])]:
			check[tuple(nums[:num+1])] = tempres + nums[num]
		else:
			check[tuple(nums[:num+1])] = check[tuple(nums[:num])]


	return check[tuple(nums)]




def rob2(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        check = {}
        ip = tuple(nums)
        check[()] = 0
        check[ip[0],] = ip[0]
        
        for i in range(1,len(ip)):
            
            temp_res = check[ip[:i-1]]
            
            if temp_res + ip[i] > check[ip[:i]]:
                check[ip[:i+1]] = temp_res + ip[i]
            else:
                check[ip[:i+1]] = check[ip[:i]]
        
        return check[ip]





print rob([2,1,1,2,4,6,10,11,8])
print rob2([2,1,1,2,4,6,10,11,8])
