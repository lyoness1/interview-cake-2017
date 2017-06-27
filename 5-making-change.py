# INPUT: integer amount, list of demoninations
# OUTPUT: integer num ways to make amount with demoninations
# RUNTIME: 

def find_num_ways(amount, demoninations):
	"""
		>>> amount = 4
		>>> demoninations = [1, 2, 3]
		>>> find_num_ways(amount, demoninations)
		4
	"""
	ways_to_make_index_cents = [0] * (amount + 1)  # index: amount, value: num_ways
	ways_to_make_index_cents[0] = 1  # There is one way to make zero cents: nothing

	for coin in demoninations:
		for total in range(coin, amount + 1):
			remainder = total - coin
			ways_to_make_index_cents[total] += ways_to_make_index_cents[remainder]

	return ways_to_make_index_cents[amount]



if __name__ == '__main__':
	import doctest
	if doctest.testmod().failed == 0:
		print "\n\nALL TESTS PASSED!!\n\n"