# Favor speeding up getter fn's over insert fn
# get_mean returns float, others return ints
# Temps all inserted as ints
# Temps recorded in deg F [0...110]
# If more than one mode, return any
class TempTracker:
	def __init__(self):
		self.temps = {}
		self.count = 0
		self.total = 0
		self.max = None
		self.min = None
		self.mean = None
		self.mode = None
		self.mode_count = 0

	def insert(self, temp):
		"""records a new temperature"""
		self.temps[temp] += 1 if self.temps[temp] else self.temps[temp] = 1
		self.count += 1
		self.total += temp
		self.max = max(self.max, temp)
		self.min = min(self.min, temp)
		self.mean = float(self.total / self.count)
		if self.temps[temp] > self.mode_count:
			self.mode_count = self.temps[temp]
			self.mode = temp

	def get_max(self):
		"""returns the highest temp seen so far"""
		return self.max

	def get_min(self):
		"""returns the lowest temp seen so far"""
		return self.min

	def get_mean(self):
		"""returns the mean of all temps"""
		return self.mean

	def get_mode(self):
		"""returns the mode of all temps"""
		return self.mode
