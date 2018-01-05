# ALGORITHM 1 Construction Base b Expansions
def expansion(n, b):
	q = n
	res = list()
	while q not 0:
		a = q%b
		q = q/b
		res.insert(0, a)
	
	return res
