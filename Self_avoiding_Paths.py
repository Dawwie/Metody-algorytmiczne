class grid:
	grid = []
	size = 0
	paths = 0
	x = 0
	y = 0
	def __init__(self, pathLength):
		self.size = pathLength + 1
		self.x = pathLength
		self.y = pathLength
		self.pathLength = pathLength
		self.paths = 0
		self.grid = range(0, self.size)
		for x in range(0, self.size):
			self.grid[x] = range(0, self.size)
			for y in range(0, self.size):
				self.grid[x][y] = 0

	def setStart(self, x, y):
		self.grid[x][y] = 1

	def move(self, x, y, moves):
		moves += 1
		if moves < self.pathLength + 1:
			self.grid[x][y] = 1
			if x == self.x - 1 and y == self.y - 1 or moves == self.pathLength:
				self.paths += 1
			else:
				if x < self.size - 1 and 0 == self.grid[x + 1][y]:
					self.move(x + 1, y, moves)
				if x > 0 and y < self.size - 1 and y != 0 and 0 == self.grid[x - 1][y]:
					self.move(x - 1, y, moves)
				if y < self.size - 1 and 0 == self.grid[x][y + 1]:
					self.move(x, y + 1, moves)
				if y > 0 and x > 0 and x < self.size - 1 and 0 == self.grid[x][y - 1]:
					self.move(x, y - 1, moves)
			self.grid[x][y] = 0

	def getPathCount(self):
		return (self.paths * 2 * 4) - 2

grid = grid(4)
grid.move(0, 1, 0)
grid.setStart(0, 0)
print grid.getPathCount()
