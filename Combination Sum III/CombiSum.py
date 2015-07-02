

def CombiSum(k,n):
	result = []
	tempSum = []
	Calculate(result,1,k,tempSum,n)
	return result

def Calculate(result,start,k,tempSum,n):
	if n == 0 and k == 0 :
		result.append(list(tempSum))

	elif k < 0 or n < 0:
		return 


	for i in range(start,10):	

		tempSum.append(i)
		Calculate(result,i+1,k-1,tempSum,n-start)
		tempSum.pop()
		start += 1
		
print CombiSum(3,9)
