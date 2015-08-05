def isInterleave(s1, s2, s3):
	result = []
	out = interLeave(s1,s2,s3)
	return out



def interLeave(s1,s2,s3):

	# base cases
	if len(s1) + len(s2) != len(s3):
		return False

	if s1 + s2 == s3 or s2 + s1 == s3:
		return True

	check = [[False for j in range(len(s2)+1)] for i in range(len(s1)+1)]

	check[0][0] = True
	
	#check s1 with s3
	for i in range(1,len(s1)+1):
		check[i][0] = check[i-1][0] and s1[i-1] == s3[i-1]

	for j in range(1,len(s2)+1):
		check[0][j] = check[0][j-1] and s2[j-1] == s3[j-1]

	for i in range(1,len(s1)+1):
		for j in range(1,len(s2)+1):
			check[i][j] = (s1[i-1] == s3[i+j-1] and check[i-1][j]) or (s2[j-1] == s3[i+j-1] and check[i][j-1])
	return check[len(s1)][len(s2)]



def isInterleave2(s1, s2, s3): 
     if len(s1) + len(s2) != len(s3): 
         return False 
     match = [[False for i in xrange(len(s2) + 1)] for j in xrange(len(s1) + 1)] 
     match[0][0] = True 
     for i in xrange(1, len(s1) + 1): 
         match[i][0] = match[i - 1][0] and s1[i - 1] == s3[i - 1] 
     for j in xrange(1, len(s2) + 1): 
         match[0][j] = match[0][j - 1] and s2[j - 1] == s3[j - 1] 
     for i in xrange(1, len(s1) + 1): 
         for j in xrange(1, len(s2) + 1): 
             match[i][j] = (match[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (match[i][j - 1] and s2[j - 1] == s3[i + j - 1]) 
     return match[-1][-1] 





print isInterleave("aabcc", "dbbca", "aadbbcbcac")
print isInterleave("aabcc", "dbbca", "aadbbbaccc")
print isInterleave(  "ab", "bc", "babc")

print ""

print isInterleave2("aabcc", "dbbca", "aadbbcbcac")
print isInterleave2("aabcc", "dbbca", "aadbbbaccc")
print isInterleave2(  "ab", "bc", "babc")
