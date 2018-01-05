# CH4.3 ALGORITHM 1 The Euclidean Algorithm

def gcd(a,b):
	x = a
	y = b
	while y <> 0:
		r = x%y
		x = y
		y = r
	return x

print(gcd(12,18))
print(gcd(111, 201))
print(gcd(1001, 1331))
print(gcd(12345, 54321))
print(gcd(1000, 5040))
print(gcd(9888, 6060))

