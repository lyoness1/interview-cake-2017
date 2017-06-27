# INPUT: 2 dictx, rectangles
# OUTPUT: dict, rectangular intersection
# RUNTIME: O(1)

def find_rectangular_intersection(rect_1, rect_2):
	"""
		>>> rect_1 = {'left_x': 1, 'bottom_y': 5, 'width': 10, 'height': 4}
		>>> rect_2 = {'left_x': 0, 'bottom_y': 4, 'width': 2, 'height': 2}
		>>> find_rectangular_intersection(rect_1, rect_2)
		{'width': 1, 'left_x': 1, 'bottom_y': 5, 'height': 1}
		>>> rect_1 = {'left_x': 1, 'bottom_y': 5, 'width': 10, 'height': 4}
		>>> rect_2 = {'left_x': 0, 'bottom_y': 8, 'width': 2, 'height': 2}
		>>> find_rectangular_intersection(rect_1, rect_2)
		{'width': 1, 'left_x': 1, 'bottom_y': 8, 'height': 1}
		>>> rect_1 = {'left_x': 1, 'bottom_y': 5, 'width': 10, 'height': 4}
		>>> rect_2 = {'left_x': 4, 'bottom_y': 4, 'width': 2, 'height': 2}
		>>> find_rectangular_intersection(rect_1, rect_2)
		{'width': 2, 'left_x': 4, 'bottom_y': 5, 'height': 1}
		>>> rect_1 = {'left_x': 1, 'bottom_y': 5, 'width': 10, 'height': 4}
		>>> rect_2 = {'left_x': 4, 'bottom_y': 8, 'width': 2, 'height': 2}
		>>> find_rectangular_intersection(rect_1, rect_2)
		{'width': 2, 'left_x': 4, 'bottom_y': 8, 'height': 1}
		>>> rect_1 = {'left_x': 1, 'bottom_y': 5, 'width': 10, 'height': 4}
		>>> rect_2 = {'left_x': 6, 'bottom_y': 7, 'width': 1, 'height': 1}
		>>> find_rectangular_intersection(rect_1, rect_2)
		{'width': 1, 'left_x': 6, 'bottom_y': 7, 'height': 1}
		>>> rect_1 = {'left_x': 1, 'bottom_y': 5, 'width': 10, 'height': 4}
		>>> rect_2 = {'left_x': 8, 'bottom_y': 4, 'width': 1, 'height': 6}
		>>> find_rectangular_intersection(rect_1, rect_2)
		{'width': 1, 'left_x': 8, 'bottom_y': 5, 'height': 4}
		>>> rect_1 = {'left_x': 1, 'bottom_y': 5, 'width': 10, 'height': 4}
		>>> rect_2 = {'left_x': 10, 'bottom_y': 4, 'width': 2, 'height': 2}
		>>> find_rectangular_intersection(rect_1, rect_2)
		{'width': 1, 'left_x': 10, 'bottom_y': 5, 'height': 1}
		>>> rect_1 = {'left_x': 1, 'bottom_y': 5, 'width': 10, 'height': 4}
		>>> rect_2 = {'left_x': 10, 'bottom_y': 7, 'width': 2, 'height': 1}
		>>> find_rectangular_intersection(rect_1, rect_2)
		{'width': 1, 'left_x': 10, 'bottom_y': 7, 'height': 1}
	"""
	intersection = {}
	intersection['left_x'] = max(rect_1['left_x'], rect_2['left_x'])
	intersection['bottom_y'] = max(rect_1['bottom_y'], rect_2['bottom_y'])

	rect_1['right_x'] = rect_1['left_x'] + rect_1['width']
	rect_2['right_x'] = rect_2['left_x'] + rect_2['width']
	intersection_right_x = min(rect_1['right_x'], rect_2['right_x'])
	intersection['width'] = intersection_right_x - intersection['left_x']

	rect_1['top_y'] = rect_1['bottom_y'] + rect_1['height']
	rect_2['top_y'] = rect_2['bottom_y'] + rect_2['height']
	intersection_top_y = min(rect_1['top_y'], rect_2['top_y'])
	intersection['height'] = intersection_top_y - intersection['bottom_y']

	return intersection


if __name__ == '__main__':
	import doctest
	if doctest.testmod().failed == 0:
		print "\n\nALL TESTS PASSED!!\n\n"