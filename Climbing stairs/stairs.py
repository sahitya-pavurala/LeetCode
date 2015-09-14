def stairs(n,steps=[1,2]):

	check = {}
	check[1] = 1
	check[2] = 2

	if n <= 2:
		return n

	for i in range(3,n+1):

		check[i] = check[i-1] + check[i-2]

	return check[n]


def stairs2(n,stairs=[1,2]):

	check1 = 1
	check2 = 2

	if n <=2:
		return n

	for i in range(3,n+1):

		check2 += check1

		check1 = check2 - check1

	return check2









print stairs(8)
print stairs2(8)