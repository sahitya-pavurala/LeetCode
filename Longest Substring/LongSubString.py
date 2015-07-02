def LCS(a,b):
	max_index = 0
	word1 = list(a)
	word2 = list(b)
	lsuff = [[0]*(len(word2)+1) for i in range(len(word1)+1)]
	end_index = 0

	for i in range(0,len(word1)+1):
		for j in range(0,len(word2)+1):

			if i == 0  or j == 0:
					lsuff[i][j] = 0

			else :
				if (word1[i-1] == word2[j-1]):
					lsuff[i][j] = lsuff[i-1][j-1] + 1 

					if(max_index < lsuff[i][j]):

						max_index = lsuff[i][j]
						end_index = i
				else:
					lsuff[i][j] = 0
	
	print max_index
	print end_index
	return word1[end_index-max_index:end_index]


print ''.join(LCS("loageeksstuff","abbageeks"))
print ''.join(LCS("geeksstuff","geeks"))
print ''.join(LCS("abba geeku","abba geeksu"))
print ''.join(LCS("rave ninu dengutha","abbo ninu dengali"))
print ''.join(LCS("abba geeku","oageeks"))



