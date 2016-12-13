"""
path1 = [[1, "s"], [2, "w"]]
path2 = path1[:]
path2.append([3, "E"])
path3 = path2[:]
path3.append([4, "N"])
print path1, "\n", path2, "\n", path3
"""
import Queue


board =
# board[row][colom]
def koffie(z):
	print "steps:", len(z.pathWay), ", path:", z.pathWay
	for i in range(len(z.start)):
		row= str(z.start[i])
		print z.start[i]
	print "\n"

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
        print children
        winning_board = 0
        won = 0
        for each in children:
            if not str(each.start) in archive:
                archive[str(each.start)] = str(each.start)
                # loop over board rows
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
            if counter % 50000 == 0:
                print "counter:", counter/1000000, "million", ", queue:", queue.qsize(), ", archive size:", len(archive)

def astar():


    def heuristics(board):
        cost = 0
        for i in range(0, board.height):
            if 1 in board.start[i]:
                for j in range(0, board.width):
                    if board.start[i][j] != 0 and board.start[i][j] != 1:
                        cost += 10
                    	for k in range(0, board.height):
                    		if board.start[k][j] != 0:
                    			cost += 5

                          
        return cost
                    
    # initialize the starting board
    boarding = Board(board)
    # create archive/ closed list
    archive_astar = dict()
    # create open list 
    priority = Queue.PriorityQueue()
    # put starting board in queue
    priority.put((0, boarding))
    counter = 0
    # for calculating path
    came_from = {}
    # calculates cost made so far
    cost_so_far = {}
    # starting board came from nowhere
    came_from[boarding] = 0
    # no costs either
    cost_so_far[boarding] = 0
    won = 0
    childcost= 0
    winning_board = 0
    # until there are no more positions and more nodes to traverse
    while not priority.empty():
        
        # get first board
        score, boarding = priority.get()
        # make children of that board
        childrens = boarding.children()
        # for each child that in archive
        for child in childrens:
        	counter += 1
        	childCost = cost_so_far[boarding] + 1

        	if not str(child.start) in archive_astar:
        		cost_so_far[child] = childCost
        		total = cost_so_far[child] + heuristics(child)
        		priority.put( (total, child))
        		came_from[child] = boarding
        		archive_astar[str(child.start)] = (child.start)
        		for i in range(boarding.height):
        			if 1 in child.start[i]:
        				for j in range(boarding.width):
        					if child.start[i][j] == 1:
        						won = 0
        					elif not child.start[i][j] == 0:
        						won += 1
        		if won == 0:
        			print "won 1\n"
        			return child
        		else:
        			archive_astar[str(child.start)] = (child.start)
        			if counter % 1000 == 0:
        				print "counter", counter, "queue", priority.qsize(), ", archive size:", len(archive_astar)
	  
            
    return came_from, cost_so_far



winning = astar()
print dir(winning)
koffie(winning)


#.pathWay, len(winning.pathWay)
#for i in range(len(winning.start)):
#	print winning.start[i]

    


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



#winning = astar()
#print winning.pathWay, len(winning.pathWay)
#for i in range(len(winning.start)):
#	print winning.start[i]



# depth first: game 4, ong 5 minuten, 7416 stappen.

