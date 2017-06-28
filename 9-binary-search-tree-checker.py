# Valid BST:
# 	1. Node's value is greater than all values in left subtree
# 	2. Node's value is less than all values in right subtree

"""
	>>> node_1 = BinaryTreeNode(1)
	>>> node_2 = BinaryTreeNode(2)
	>>> node_3 = BinaryTreeNode(3)
	>>> node_4 = BinaryTreeNode(4)
	>>> node_5 = BinaryTreeNode(5)
	>>> node_3.is_valid_bst()
	True
	>>> node_3.insert_left(node_2)
	>>> node_3.insert_right(node_5)
	>>> node_3.is_valid_bst()
	True
	>>> node_2.insert_left(node_1)
	>>> node_3.is_valid_bst()
	True
	>>> node_5.insert_left(node_4)
	>>> node_3.is_valid_bst()
	True
	>>> node_4.insert_left(node_1)
	>>> node_3.is_valid_bst()
	False
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

	def is_valid_bst(self):
		min_val = float('-inf')
		max_val = float('inf')

		def _is_valid_bst(node, min_val, max_val):
			if node.value < min_val or node.value > max_val:
				return False

			if node.left and not _is_valid_bst(node.left, min_val, node.value):
				return False
			if node.right and not _is_valid_bst(node.right, node.value, max_val):
				return False

			return True

		return _is_valid_bst(self, min_val, max_val)


if __name__ == '__main__':
	import doctest
	if doctest.testmod().failed == 0:
		print "\n ALL TESTS PASSED!! \n"
