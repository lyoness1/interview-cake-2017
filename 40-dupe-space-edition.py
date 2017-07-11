
def find_dupe_space_optomized(arr):
	"""Returns all duplicates in arr
		>>> find_dupe_space_optomized([1, 2, 3, 4, 5, 6, 6, 7, 8, 9])
		[6]
        >>> find_dupe_space_optomized([1, 2, 3, 3, 5, 6, 7, 7, 7, 9])
        [3, 7]
	"""
	arr.sort()
	output = []
	for i in xrange(len(arr) - 2):
		if arr[i] == arr[i+1] and arr[i] not in output:
			output.append(arr[i])
	return output




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
