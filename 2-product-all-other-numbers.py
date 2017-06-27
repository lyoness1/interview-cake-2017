# INPUT: List of integers.
# OUTPUT: List of integers 
# RUNTIME: O(n)

def get_products_of_all_ints_except_at_index(ints):
	"""
		>>> ints = [1, 7, 3, 4]
		>>> get_products_of_all_ints_except_at_index(ints)
		[84, 12, 28, 21]
		>>> ints = [1]
		>>> get_products_of_all_ints_except_at_index(ints)
		'List must be at least two integers long'
		>>> ints = [1, 2]
		>>> get_products_of_all_ints_except_at_index(ints)
		'List must be at least two integers long'
		>>> ints = [0, 1, 2, 3]
		>>> get_products_of_all_ints_except_at_index(ints)
		[6, 0, 0, 0]
		>>> ints = [5, 0, 0]
		>>> get_products_of_all_ints_except_at_index(ints)
		[0, 0, 0]
		>>> ints = [-1, 2, 3]
		>>> get_products_of_all_ints_except_at_index(ints)
		[6, -3, -2]
		>>> ints = [-1, -2, 3]
		>>> get_products_of_all_ints_except_at_index(ints)
		[-6, -3, 2]
	"""
	if len(ints) < 3:
		return 'List must be at least two integers long'

	products = [None] * len(ints)
	forward_product = 1
	backwards_product = 1

	for index, num in enumerate(ints):
		products[index] = forward_product
		forward_product *= num

	for index in range(len(ints)-1, -1, -1):
		products[index] *= backwards_product
		backwards_product *= ints[index]

	return products

if __name__ == '__main__':
	import doctest
	if doctest.testmod().failed == 0:
		print "\n\nALL TESTS PASSED!!\n\n"