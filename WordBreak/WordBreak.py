

def WordBreak(s, words):

	check = [False for i in range(len(s)+2)]

	check[0] = True #Initial state

	for i in range(len(s)+1):

		for word in words:
			end = len(word) + i

			if (end > len(s)):
				continue

			elif s[i:end] == word and check[i]:
				check[end] = True

			if(check[len(s)]):
				return True 
					  
	return check[len(s)]		


print WordBreak("iamlegend",["leg","i","am","start","end"])
print WordBreak("iamlegend",["leg","am","start","end"])
print WordBreak("iamlegend",["legend","i","am"])
print WordBreak("iamlegend",["legen","i","am"])
print WordBreak("iamlegend",["legen","i","am","legend"])