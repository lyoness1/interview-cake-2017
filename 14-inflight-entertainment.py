# Eh... this is a pretty naive n^solution. 
def determine_best_movies(flight_length, movie_lengths):
	"""
        >>> determine_best_movies(120, [45, 60, 70, 40, 60, 110, 80, 130])
        True
        >>> determine_best_movies(120, [45, 60, 110, 30])
        False
	"""
	movie_lengths.sort()
	for idx, movie in enumerate(movie_lengths):
		remainder = flight_length - movie
		if remainder < 0:
			return False
		for next_movie in movie_lengths[idx+1:]:
			if next_movie == remainder:
				return True
	return False

# This is O(n)
def determine_best_movies_again(flight_length, movie_lengths):
	"""
        >>> determine_best_movies_again(120, [45, 60, 70, 40, 60, 110, 80, 130])
        True
        >>> determine_best_movies_again(120, [45, 60, 110, 30])
        False
	"""
	lengths = set(movie_lengths)
	while lengths:
		movie = lengths.pop()
		remainder = flight_length - movie
		if remainder in lengths:
			return True
	return False

if __name__ == '__main__':
	import doctest
	if doctest.testmod().failed == 0:
		print "\n\nALL TESTS PASSED!!\n\n"