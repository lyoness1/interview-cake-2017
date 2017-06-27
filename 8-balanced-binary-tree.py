class BinaryTreeNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert_left(self, value):
		self.left = BinaryTreeNode(value)
		return self.left

	def insert_right(self, value):
		self.right = BinaryTreeNode(value)
		return self.right

	def is_leaf(self):
		return (not self.left and not self.right)


class BinaryTree:
	def __init__(self, root=None):
		if root:
			assert isinstance(root, BinaryTreeNode), "Root must be a BinaryTreeNode"
		self.root = root
		self.min_depth = float('inf')
		self.max_depth = float('-inf')

	def reset(self):
		self.min_depth = float('inf')
		self.max_depth = float('-inf')

	def is_superbalanced(self, curr_node=None, curr_depth=0):
		"""Determines if the maximum depth between any two leaf nodes is at most one."""
		if not curr_node:
			curr_node = self.root

		if curr_node.is_leaf():
			self.min_depth = min(self.min_depth, curr_depth) 
			self.max_depth = max(self.max_depth, curr_depth)
		if curr_node.right:
			self.is_superbalanced(curr_node.right, curr_depth + 1)
		if curr_node.left:
			self.is_superbalanced(curr_node.left, curr_depth + 1)
		
		return (self.max_depth - self.min_depth <= 1)


if __name__ == '__main__':
	tree = BinaryTree(BinaryTreeNode('a'))
	print tree.is_superbalanced()
	tree.reset()

	tree.root.insert_right('b')
	print tree.is_superbalanced()
	tree.reset()

	tree.root.right.insert_right('c')
	print tree.is_superbalanced()
	tree.reset()

	tree.root.insert_left('d')
	print tree.is_superbalanced()
	tree.reset()

	tree.root.right.right.insert_right('e')
	print tree.is_superbalanced()