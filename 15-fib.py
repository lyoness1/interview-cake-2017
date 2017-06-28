# Index: 0, 1, 2, 3, 4, 5, 6, 7,  8, ...
# Fib #: 0, 1, 1, 2, 3, 5, 8, 13, 21,...

def fib(idx):
	"""
		>>> fib(0)
		0
		>>> fib(1)
		1
		>>> fib(2)
		1
		>>> fib(3)
		2
		>>> fib(8)
		21
	"""
	fib_base = [0, 1]
	if idx < 2:
		return fib_base[idx]

	prev_2 = fib_base[0]
	prev_1 = fib_base[1]
	for i in xrange(2, idx+1):
		fib = prev_1 + prev_2
		prev_2 = prev_1
		prev_1 = fib

	return fib

if __name__ == '__main__':
	import doctest
	if doctest.testmod().failed == 0:
		print "\n\nALL TESTS PASSED!!\n\n"
