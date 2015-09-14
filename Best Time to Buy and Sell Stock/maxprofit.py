'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''


def maxprofit(nums):

	max_profit = nums[0]
	min_val = nums[0]
	

	for i in range(1,len(nums)):

		if nums[i] < min_val :
			min_val = nums[i]
			continue

		else :
			temp = nums[i] - min_val
			if temp > max_profit:
				max_profit = temp

	return max_profit
	