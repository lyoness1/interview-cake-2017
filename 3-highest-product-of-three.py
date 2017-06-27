# INPUT: List of integers.
# OUTPUT: Integer
# RUNTIME: ln(n)

def get_highest_product_of_three(ints):
	"""
		>>> ints = [1, 2, 3, 4]
		>>> get_highest_product_of_three(ints)
		24
		>>> ints = [1]
		>>> get_highest_product_of_three(ints)
		'List must be at least three integers long'
		>>> ints = [4, 3, 2, 6]
		>>> get_highest_product_of_three(ints)
		72
		>>> ints = [1, 0, 0, 0]
		>>> get_highest_product_of_three(ints)
		0
		>>> ints = [1, -1, 2, 3]
		>>> get_highest_product_of_three(ints)
		6
		>>> ints = [-2, -3, -4, -5]
		>>> get_highest_product_of_three(ints)
		-24
		>>> ints = [-2, -3, -4, 5]
		>>> get_highest_product_of_three(ints)
		60
	"""
	if len(ints) < 3:
		return 'List must be at least three integers long'

	values = sorted(ints)
	return max(
		values[0] * values[1] * values[2],
		values[0] * values[1] * values[-1],
		values[0] * values[-2] * values[-1],
		values[-3] * values[-2] * values[-1]
	)
	

if __name__ == '__main__':
	import doctest
	if doctest.testmod().failed == 0:
		print "\n\nALL TESTS PASSED!!\n\n"