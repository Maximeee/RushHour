"""
path1 = [[1, "s"], [2, "w"]]
path2 = path1[:]
path2.append([3, "E"])
path3 = path2[:]
path3.append([4, "N"])
print path1, "\n", path2, "\n", path3
"""
import Queue

board = [
[0,0,3,2,2,4],
[0,0,3,0,0,4],
[0,0,3,1,1,4],
[0,0,0,5,6,6],
[7,8,8,5,0,0],
[7,0,0,5,9,9]
]
# board[row][colom]
class Board(object):
	def __init__ (self, board):
		self.start = board
		self.height = len(self.start)
		self.width = len(self.start[0])

		self.vertical = dict()
		self.horizontal = dict()
		self.pathWay = []

		for i in range(0, self.height):
			for j in range(0, self.width):
				if self.start[i][j] != 0:
					if i+1 < self.height:
						if self.start[i+1][j] == self.start[i][j]:
							if not self.start[i][j] in self.vertical:
								self.vertical[self.start[i][j]] = 0
					if j+1 < self.width:
						if self.start[i][j+1] == self.start[i][j]:
							if not self.start[i][j] in self.horizontal:
								self.horizontal[self.start[i][j]] = 0
				if self.start[i][j] in self.vertical:
					self.vertical[self.start[i][j]] += 1
				elif self.start[i][j] in self.horizontal:
					self.horizontal[self.start[i][j]] += 1
	# end __init__
# print "vertical", vertical, "\nhorizontal", horizontal
	def children(self):
		new_boards = []
		for i in range(self.height):
			for j in range(self.width):
				if self.start[i][j] in self.vertical:
					empty = self.vertical[self.start[i][j]] - 1
					if i < self.height - 1:
						# omlaag
						if self.start[i+1][j] == 0:
							new_board = self.start[:]
							new_board[i - empty] = self.start[i - empty][:]
							new_board[i - empty][j] = 0
							new_board[i+1] = self.start[i+1][:]
							new_board[i+1][j] = self.start[i][j]
							temp = Board(new_board)
							temp.pathWay = self.pathWay[:]
							temp.pathWay.append([self.start[i][j], "S"])
							new_boards.append(temp)
					if i > 0:
						# omhoog
						if self.start[i-1][j] == 0:
							new_board = self.start[:]
							new_board[i + empty] = self.start[i + empty][:]
							new_board[i + empty][j] = 0
							new_board[i-1] = self.start[i-1][:]
							new_board[i-1][j] = self.start[i][j]
							temp = Board(new_board)
							temp.pathWay = self.pathWay[:]
							temp.pathWay.append([self.start[i][j], "N"])
							new_boards.append(temp)
				if self.start[i][j] in self.horizontal:
					empty = self.horizontal[self.start[i][j]] - 1
					if j + 1 < self.width:
						# rechts
						if self.start[i][j+1] == 0:
							new_board = self.start[:]
							new_board[i] = self.start[i][:]
							new_board[i][j + 1] = self.start[i][j]
							new_board[i][j - empty] = 0
							temp = Board(new_board)
							temp.pathWay = self.pathWay[:]
							temp.pathWay.append([self.start[i][j], "E"])
							new_boards.append(temp)
					if j > 0:
						# links
						if self.start[i][j-1] == 0:
							new_board = self.start[:]
							new_board[i] = self.start[i][:]
							new_board[i][j-1] = self.start[i][j]
							new_board[i][j + empty] = 0
							temp = Board(new_board)
							temp.pathWay = self.pathWay[:]
							temp.pathWay.append([self.start[i][j], "W"])
							new_boards.append(temp)
		return new_boards
		
def bf():
	parent = Board(board)
	"""
	# indicate start and print 1st board
	print "start\n"
	for i in range(len(parent.start)):
		print parent.start[i]
	print "\n"
	##
	# create archive, put start board in it
	"""
	archive = dict()
	archive[str(parent.start)] = str(parent.start)
	# create queue, put start board in it
	queue = Queue.Queue()
	queue.put(parent)
	counter = 1
	while not queue.empty():
		first = queue.get()
		# create children
		children = first.children()
		# print children
		winning_board = 0
		won = 0
		for each in children:
			if not str(each.start) in archive:
				archive[str(each.start)] = str(each.start)
				for i in range(parent.height):
					if 1 in each.start[i]:
						for j in range(parent.width):
							if each.start[i][j] == 1:
								won = 0
							elif not each.start[i][j] == 0:
								won += 1
				if won == 0:
					print "\nwon 1"
					return each
				else:
					queue.put(each)
					print "queue", queue.qsize()
			counter += 1
			if counter%1000 == 0:
				print "counter", counter, "queue", queue.qsize(), ", archive size:", len(archive)
	#end of while loop

def df():
	parent = Board(board)
	"""
	# indicate start and print 1st board
	print "start\n"
	for i in range(len(parent.start)):
		print parent.start[i]
	print "\n"
	##
	# create archive, put start board in it
	"""
	archive = dict()
	archive[str(parent.start)] = str(parent.start)
	# create queue, put start board in it
	stack = []
	stack.append(parent)
	counter = 1
	while not len(stack) == 0:
		first = stack.pop(0)
		# create children
		children = first.children()
		# print children
		winning_board = 0
		won = 0
		for each in children:
			if not str(each.start) in archive:
				archive[str(each.start)] = str(each.start)
				for i in range(parent.height):
					if 1 in each.start[i]:
						for j in range(parent.width):
							if each.start[i][j] == 1:
								won = 0
							elif not each.start[i][j] == 0:
								won += 1
				if won == 0:
					print "\nwon 1"
					return each
				else:
					stack.insert(0, each)
					print "queue", len(stack)
			counter += 1
			steps +=1
			print "counter", counter, "stack", len(stack), ", archive size:", len(archive)

	#end of while loop	



winning = df()
print winning.pathWay, len(winning.pathWay)
for i in range(len(winning.start)):
	print winning.start[i]



# depth first: game 4, ong 5 minuten, 7416 stappen.