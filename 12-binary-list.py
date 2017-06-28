def find_integer_in_sorted_list(sorted_list, num):
	"""
		>>> arr = [1, 2, 3, 5, 8, 10, 34]
		>>> find_integer_in_sorted_list(arr, 8)
		True
		>>> find_integer_in_sorted_list(arr, 17)
		False
	"""

	count = len(sorted_list)  
	mid = count / 2
	high = count - 1
	low = 0
	guess = None

	while (high - low) > 1 and guess != num:
		guess = sorted_list[mid]
		if guess < num:
			low = mid
			mid = (high - low) / 2 + low
		if guess > num:
			high = mid
			mid = (high - low) / 2

	return guess == num


if __name__ == '__main__':
	import doctest
	if doctest.testmod().failed == 0:
		print "\n\nALL TESTS PASSED!!\n\n"