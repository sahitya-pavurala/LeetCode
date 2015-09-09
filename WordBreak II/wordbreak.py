def WordBreak(s, words):

	"""
	:type s: str
	:type wordDict: Set[str]
	:rtype: List[str]
	"""


	check = [False for i in range(len(s)+2)]
	check[0] = True #Initial state

	result = [[] for i in range(len(s)+2)]


	for i in range(len(s)+1):
		for word in words:

			end = len(word) + i
			if s[i:end] == word and check[i]:
				check[end] = True
				result[i].append(end)

	final_result = []

	if not check[len(s)]:
		return final_result

	def recurse(idx,current_result):

		for n in result[idx]:
			new_result = current_result + " " + s[idx:n] if current_result else s[idx:n]

			if n == len(s):
				final_result.append(new_result)
			else:
				recurse(n,new_result)


	recurse(0,"")

	return final_result



	

print WordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"])