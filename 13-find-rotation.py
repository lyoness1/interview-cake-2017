def find_rotation_index(words):
	"""
		>>> words = ['horse', 'zebra', 'bat', 'cat', 'dog']
		>>> find_rotation_index(words)
		2
		>>> words = ['bat', 'cat', 'dog', 'horse', 'zebra']
		>>> find_rotation_index(words)
		0
		>>> words = ['cat', 'dog', 'horse', 'zebra', 'bat']
		>>> find_rotation_index(words)
		4
	"""
	if words[0] < words[-1]:
		return 0
		
	right_index = len(words) - 1
	left_index = 0

	while right_index - left_index > 1:
		guess_index = left_index + (right_index - left_index) / 2
		if words[guess_index] < words[right_index]:
			right_index = guess_index
		left_index = guess_index

	return right_index


	


if __name__ == '__main__':
	import doctest
	if doctest.testmod().failed == 0:
		print "\n\nALL TESTS PASSED!!\n\n"