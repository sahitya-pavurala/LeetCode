def shortestPalindrome(s):

	original = list(s)
	rev = reversed(original)
	common = LongSubString(original,rev)

	if s.index(common) == 0:
		return s[len(common):][::-1] + s

	else:
		return s[1:][::-1] + s

	
def LongSubString(a,b):
	max_len = 0
	end_index = 0
	word1 = list(a)
	word2 = list(b)
	LCSuff = [[0]*(len(word2)+1) for x in range(len(word1)+1)]

	for i in range(len(word1)+1):
		for j in range(len(word2)+1):

			if(i == 0 or j ==0):	
				LCSuff[i][j] = 0

			else:
				if(word1[i-1] == word2[j-1]):
					LCSuff[i][j] = LCSuff[i-1][j-1] +1
					if(max_len < LCSuff[i][j]):
						max_len = LCSuff[i][j]
						end_index = i
				else:
					LCSuff[i][j] = 0

	return ''.join(word1[end_index-max_len:end_index])








print shortestPalindrome("abcd")
print shortestPalindrome("aacecaaa")
print shortestPalindrome("eeks")
print shortestPalindrome("geeks")
print shortestPalindrome("ageeks")
print shortestPalindrome("aheeogeeks")
