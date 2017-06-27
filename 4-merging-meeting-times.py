# INPUT: List of tuples. 
# OUTPUT: List of tuples.
# RUNTIME: ln(n) to sort, n to iterate => O(n)

def merge_ranges(meetings):
	"""
		>>> meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
		>>> merge_ranges(meetings)
		[(0, 1), (3, 8), (9, 12)]
	"""
	sorted_meetings = sorted(meetings, key=lambda t: t[0])
	merged = [sorted_meetings[0]]

	for meeting in sorted_meetings[1:]:
		curr_start, curr_end = merged[-1]
		start_time, end_time = meeting
		# overlap
		if start_time <= curr_end:
			merged[-1] = (curr_start, end_time)
		# no overlap
		else:
			merged.append((start_time, end_time))

	return merged


if __name__ == '__main__':
	import doctest
	if doctest.testmod().failed == 0:
		print "\n\nALL TESTS PASSED!!\n\n"