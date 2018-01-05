# ALGORITHM 2 Addition of two binary integers
def binadd(a, b):
	res = list()
	n = max(len(str(a)), len(str(b)))-1
	c = 0
	while n >= 0:
		d = (int(str(a)[n])+int(str(b)[n])+c)/2
		s = int(str(a)[n])+int(str(b)[n])+c - 2*d
		res.insert(0, s)
		c = d
		n -= 1
	res.insert(0, c)

	return res
