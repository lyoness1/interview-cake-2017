"""
	>>> node_3 = BinaryTreeNode(3)
	>>> node_3.find_second_largest_value_in_subtree()
	'Tree must have at least two values'
	>>> node_2 = BinaryTreeNode(2)
	>>> node_3.insert_left(node_2)
	>>> node_3.find_second_largest_value_in_subtree()
	2
	>>> node_5 = BinaryTreeNode(5)
	>>> node_3.insert_right(node_5)
	>>> node_3.find_second_largest_value_in_subtree()
	3
	>>> node_5.insert_right(BinaryTreeNode(6))
	>>> node_3.find_second_largest_value_in_subtree()
	5
	>>> node_4 = BinaryTreeNode(4)
	>>> node_5.insert_left(node_4)
	>>> node_3.find_second_largest_value_in_subtree()
	5
	>>> node_5.right = None	
	>>> node_3.find_second_largest_value_in_subtree()
	4
	>>> node_4.insert_right(BinaryTreeNode(4.5))
	>>> node_3.find_second_largest_value_in_subtree()
	4.5
"""

class BinaryTreeNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert_left(self, node):
		self.left = node

	def insert_right(self, node):
		self.right = node

	def is_leaf(self):
		return (not self.left and not self.right)

	def find_largest_value_and_parent(self):
		curr_node = self
		prev_node = None
		while curr_node.right != None:
			prev_node = curr_node
			curr_node = curr_node.right

		return curr_node, prev_node

	def find_second_largest_value_in_subtree(self):
		if self.is_leaf():
			return "Tree must have at least two values"

		largest_value, parent = self.find_largest_value_and_parent()
		
		if largest_value.left == None:
			return parent.value

		second_largest, parent = largest_value.left.find_largest_value_and_parent()
		return second_largest.value


if __name__ == '__main__':
	import doctest
	if doctest.testmod().failed == 0:
		print "\n\nALL TESTS PASSED!!\n\n"
