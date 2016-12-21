import Listlist_Breadth_first_vizualize
import Queue
import random
from datetime import datetime

tijd = datetime.now()

# imput is in de vorm [[row1],[row1],[row3],[row4], etc]
games = [
# test game
[[0,0,0,5,5,0],
[0,4,4,4,4,0],
[0,0,0,0,3,0],
[0,0,0,0,3,0],
[1,1,0,2,3,0],
[0,0,0,2,3,0],
[0,0,0,0,0,0]],
# game 1
[[0,0,3,2,2,4],[0,0,3,0,0,4],[0,0,3,1,1,4],[0,0,0,5,6,6],[7,8,8,5,0,0],[7,0,0,5,9,9]],
# game 2
[[0,0, 2, 2, 3, 3],[ 0, 4, 4, 5, 5, 6],[ 0, 0, 1, 1, 7, 6],[ 8, 8, 9, 9, 7, 6],[10, 0, 0,11,12,12],[10, 0, 0,11,13,13]],
# game 3
[[ 0, 2, 2, 3, 3, 3],[ 0, 4, 4, 5, 6, 6],[ 1, 1, 7, 5, 0, 8],[ 9, 9, 7,10,10, 8],[11, 0,12, 0,13,13],[11, 0,12, 0, 0, 0]],
# game 4
[[ 2, 3, 3, 3, 0, 4, 0, 0, 0],[ 2, 0, 0, 5, 0, 4, 6, 6, 6],[ 0, 0, 0, 5, 0, 4, 0, 0, 7],[ 8, 8, 0, 5, 0, 9, 9, 9, 7],[10, 1, 1,11, 0, 0, 0, 0, 7],[10, 0,12,11, 0,13,13,13,14],[15,15,12,16,17,17, 0, 0,14],[18, 0,12,16,19, 0, 0, 0,14],[18,20,20,20,19,21,21,22,22]],
# game 5
[[ 2, 2, 2, 3, 0, 4, 5, 0, 0],[ 0, 0, 0, 3, 0, 4, 5, 6, 6],[ 0, 0, 0, 3, 7, 7, 8, 0, 0],[ 0, 0, 0, 0, 9, 9, 8,10,10],[ 0, 0,11,11,11,12, 1, 1,13],[14, 0,15, 0, 0,12, 0, 0,13],[14, 0,15,16,16,12,17,17,13],[18,19,20,20,21,22,22,22,23],[18,19,24,24,21, 0, 0, 0,23]],
# game 6
[[ 2, 2, 3, 3, 4, 0, 0, 5, 0],[ 6, 7, 7, 7, 4, 8, 8, 5, 0],[ 6, 0, 9, 9,10,11, 0,12,12],[ 0, 0,13,14,10,11,15,15,15],[ 1, 1,13,14, 0, 0, 0, 0, 0],[ 0,16, 0,14,17,17,18,18,19],[20,16,21,21,22,23,23,23,19],[20, 0,24,24,22,25,25, 0,19],[20,26,26,26,22, 0, 0, 0 ,0]],
# game 7
[[ 2, 0, 0, 0, 0, 0, 3, 4, 4, 4, 5, 5],
[ 2, 0, 0, 0, 0, 6, 3, 0, 0, 0, 7, 8],
[ 9, 9, 9,10,10, 6,11,12,12, 0, 7, 8],
[13,14, 0, 0, 0,15,11,16,16,17,17, 0],
[13,14,18,18,18,15,11,19,19,19, 0, 0],
[13,14, 1, 1,20,21, 0, 0, 0, 0, 0, 0],
[22,22,22,23,20,21,24,28, 0,50,25,25],
[26,26,26,23,27,27,24,28, 0,50,29,29],
[30,30,31,32,32,32,24,33,33,33, 0,34],
[ 0, 0,31,35,35,35,36, 0,37,37,38,34],
[ 0, 0, 0, 0, 0, 0,36, 0, 0,39,38,40],
[ 0,41,41,42,42,42,36,43,43,49,38,40]]
]
#index of games is the board you want, index 0 is a board used for testing
chupachup = games[7]

# board[row][colom]

# accepteerd een grid en print het
def koffie(z):
	print "steps:", len(z.pathWay), ", path:", z.pathWay
	for i in range(len(z.start)):
		row = str(z.start[i])
		row.replace(" ", "")
		print z.start[i]
	print "\n"


def moveVert(board, i, j, ori):
	k = 0
	if ori == "S":
		k = 1
	elif ori == "N":
		k = -1
	empty = ((board.vertical[board.start[i][j]] - 1) * k)
	new_board = board.start[:]
	new_board[i+k] = board.start[i+k][:]
	new_board[i+k][j] = board.start[i][j]
	new_board[i - empty] = board.start[i - empty][:]
	new_board[i - empty][j] = 0
	temp = Board(new_board, board.vertical, board.horizontal)
	temp.pathWay = board.pathWay[:]
	temp.pathWay.append([board.start[i][j], ori])
	return temp

def moveHor(board, i, j, ori):
	k = 0
	if ori == "E":
		k = 1
	elif ori == "W":
		k = -1
	empty = ((board.horizontal[board.start[i][j]] - 1) * k)
	new_board = board.start[:]
	new_board[i] = board.start[i][:]
	new_board[i][j + k] = board.start[i][j]
	new_board[i][j - empty] = 0
	temp = Board(new_board, board.vertical, board.horizontal)
	temp.pathWay = board.pathWay[:]
	temp.pathWay.append([board.start[i][j], ori])
	return temp

def check_cars(board):
	vertical = dict()
	horizontal = dict()
	# loop over the board to determine which cars are horizontal or vertical
	# i loops through the rows
	# j loops through the coloms in that row
	for i in range(0, len(board)):
		for j in range(0, len(board[0])):
			# if there is a car on the current position
			if board[i][j] != 0:
				# if there is another row below that position
				if i+1 < len(board):
					# if the position underneat is has the same car on it
					if board[i+1][j] == board[i][j]:
						# if the car is not yet in the vertical dictionary
						if not board[i][j] in vertical:
							# add the id to the dictionary as key, value is the length (is updated later)
							vertical[board[i][j]] = 0
				# if there is another colom to the right of that position
				if j+1 < len(board[0]):
					# if the space to the right of the car is the same car
					if board[i][j+1] == board[i][j]:
						# if the car is not yet in the horizontal dictionary
						if not board[i][j] in horizontal:
							# add the id to the dictionary as key, value is the length (is updated later)
							horizontal[board[i][j]] = 0
			# every time a car is found on the board the length is increased
			if board[i][j] in vertical:
				vertical[board[i][j]] += 1
			elif board[i][j] in horizontal:
				horizontal[board[i][j]] += 1
	return vertical, horizontal

# checks if following steps negate eachother
def PathSweep(l):
	print "SWEEP"
	length = len(l) - 2
	while True:
		changed = 0
		for i in range(length):
			if length - i > 0 and length - i+1 < len(l):
				if l[length-i][0] == l[length-i+1][0] and not l[length-i][1] == l[length-i+1][1]:
					del l[length - i + 1]
					del l[length - i]
					changed = 1
		if changed == 0:
			return l
			break


class Board(object):
	# board opject word gemaakt aan de hand van een grid
	def __init__ (self, board, vertical, horizontal):
		self.start = board
		self.height = len(self.start)
		self.width = len(self.start[0])

		# dictionaries to store info on the cars
		self.vertical = vertical
		self.horizontal = horizontal
		# the pathWay to get to this board
		self.pathWay = []
	#### end __init__ function ####

	def children(self):
		# create an array to store the children
		new_boards = []
		# loop over the grid
		for i in range(self.height):
			for j in range(self.width):
				# check orientation of car
				if self.start[i][j] in self.vertical:
					# see how far the other end of the car is so that position can be set to 0
					# if the move is valid/ new position is still on the board
					# -1 as it is 0 indexed
					if i < self.height - 1:
						# DOWN
						# move the car down if possible
						if self.start[i+1][j] == 0:
							new_boards.append(moveVert(self, i, j, "S"))
					if i > 0:
						# UP
						# Works the same as the move down
						if self.start[i-1][j] == 0:
							new_boards.append(moveVert(self, i, j, "N"))
				# if the car found is orientated horizontally
				if self.start[i][j] in self.horizontal:
					# check the length of the car
					# and thus which position to clear
					# if a step right still is within the grid
					if j + 1 < self.width:
						# RIGHT
						# if the position to the right is empty
						if self.start[i][j+1] == 0:
							new_boards.append(moveHor(self, i, j, "E"))
					if j > 0:
						# LEFT
						# works the same as the move right
						if self.start[i][j-1] == 0:
							new_boards.append(moveHor(self, i, j, "W"))
		return new_boards

# Work in progress
def simulation(speed, board, chupachup):
	current_board = Board(chupachup, board.vertical, board.horizontal)
	anim_speed = speed
	path = board.pathWay
	# path = [[8,"S"],[8,"S"]]
	counter = 1
	anim = Listlist_Breadth_first_vizualize.RushHourVisualization(current_board, anim_speed)
	for step in path:
		counter += 1
		if step[1] == "N":
			for i in range(current_board.height):
				for j in range(current_board.width):
					if i -1 >= 0:
						if current_board.start[i][j] == step[0] and current_board.start[i-1][j] == 0:
							current_board = moveVert(current_board, i, j, step[1])
							break
		elif step[1] == "S":
			stop = 0
			for i in range(current_board.height):
				for j in range(current_board.width):
					if i +1 < current_board.height:
						if current_board.start[i][j] == step[0] and current_board.start[i+1][j] == 0:
							current_board = moveVert(current_board, i, j, step[1])
							stop = 1
							break
				if stop:
					break
		elif step[1] == "W":
			for i in range(current_board.height):
				for j in range(current_board.width):
					if j -1 >= 0:
						if current_board.start[i][j] == step[0] and current_board.start[i][j-1] == 0:
							current_board = moveHor(current_board, i, j, step[1])
							break
		elif step[1] == "E":
			for i in range(current_board.height):
				for j in range(current_board.width):
					if j+1 < current_board.width:
						if current_board.start[i][j] == step[0] and current_board.start[i][j+1] == 0:
							current_board = moveHor(current_board, i, j, step[1])
							break
		anim.update(current_board)
	anim.done()
	### end

def RandomStep():
	orientation = check_cars(chupachup)
	grid = Board(chupachup, orientation[0], orientation[1])
	maximum = 0
	for each in orientation[0]:
		if each > maximum:
			maximum = each
	for each in orientation[1]:
		if each > maximum:
			maximum = each
	counter = 0
	condition = True
	while condition:
		car = random.randint(1, maximum)
		car = int(car)
		direction = random.randint(1, 2)
		if car in orientation[0]:
			if direction == 1:
				direction = "N"
			else:
				direction= "S"
		elif car in orientation[1]:
			if direction== 1:
				direction= "E"
			else:
				direction= "W"
		step = [int(car), direction]
		if step[1] == "N":
			for i in range(grid.height):
				for j in range(grid.width):
					if i -1 >= 0:
						if grid.start[i][j] == step[0] and grid.start[i-1][j] == 0:
							grid = moveVert(grid, i, j, step[1])
							break
		elif step[1] == "S":
			stop = 0
			for i in range(grid.height):
				for j in range(grid.width):
					if i +1 < grid.height:
						if grid.start[i][j] == step[0] and grid.start[i+1][j] == 0:
							grid = moveVert(grid, i, j, step[1])
							stop = 1
							break
				if stop:
					break
		elif step[1] == "W":
			for i in range(grid.height):
				for j in range(grid.width):
					if j -1 >= 0:
						if grid.start[i][j] == step[0] and grid.start[i][j-1] == 0:
							grid = moveHor(grid, i, j, step[1])
							break
		elif step[1] == "E":
			for i in range(grid.height):
				for j in range(grid.width):
					if j+1 < grid.width:
						if grid.start[i][j] == step[0] and grid.start[i][j+1] == 0:
							grid = moveHor(grid, i, j, step[1])
							break
		else:
			continue
		for i in range(grid.height):
			if 1 in grid.start[i]:
				won = 0
				for j in range(grid.width):
					if grid.start[i][j] == 1:
						won = 0
					elif not grid.start[i][j] == 0:
						won += 1
				if won == 0:
					print "won"
					condition = False
					return grid
		counter += 1

def bf():
	###
	# paths found:
	#   board 1:
	#       [[3, 'N'], [2, 'W'], [2, 'W'], [7, 'N'], [7, 'N'], [7, 'N'], [7, 'N'], [8, 'W'], [3, 'N'], [3, 'N'], [1, 'W'], [1, 'W'], [1, 'W'], [3, 'N'], [3, 'N'], [5, 'N'], [5, 'N'], [5, 'N'], [6, 'W'], [4, 'N'], [4, 'N'], [8, 'E'], [8, 'E'], [8, 'E'], [3, 'N'], [3, 'N'], [1, 'E'], [7, 'N'], [2, 'W'], [7, 'N'], [7, 'N'], [1, 'W'], [3, 'N'], [3, 'N'], [3, 'N'], [6, 'W'], [6, 'W'], [5, 'N'], [7, 'N'], [6, 'W'], [3, 'N'], [2, 'E'], [2, 'E'], [2, 'E'], [2, 'E'], [3, 'N'], [5, 'N'], [6, 'E'], [6, 'E'], [6, 'E'], [3, 'N'], [3, 'N'], [7, 'N'], [3, 'N'], [1, 'E'], [7, 'N'], [7, 'N'], [7, 'N'], [1, 'W'], [3, 'N'], [3, 'N'], [3, 'N'], [6, 'W'], [6, 'W'], [5, 'N'], [6, 'W'], [3, 'N'], [8, 'W'], [8, 'W'], [5, 'N'], [8, 'W'], [3, 'N'], [9, 'W'], [4, 'N'], [9, 'W'], [9, 'W'], [5, 'N'], [9, 'W'], [3, 'N']]
	#   board2: time 3.302s
	#       26 steps => [[2, 'W'], [2, 'W'], [3, 'W'], [3, 'W'], [4, 'W'], [5, 'W'], [6, 'N'], [1, 'W'], [7, 'N'], [7, 'N'], [9, 'E'], [9, 'E'], [11, 'N'], [11, 'N'], [12, 'W'], [12, 'W'], [12, 'W'], [11, 'N'], [13, 'W'], [13, 'W'], [13, 'W'], [11, 'N'], [9, 'W'], [6, 'N'], [6, 'N'], [6, 'N']]
	#   board 3: time 2.42s(with prints)
	#       34 steps => [[2, 'W'], [4, 'W'], [7, 'N'], [7, 'N'], [12, 'N'], [12, 'N'], [13, 'W'], [8, 'N'], [13, 'W'], [13, 'W'], [8, 'N'], [10, 'E'], [5, 'N'], [6, 'W'], [5, 'N'], [5, 'N'], [10, 'W'], [8, 'N'], [8, 'N'], [8, 'N'], [10, 'E'], [5, 'N'], [5, 'N'], [13, 'E'], [13, 'E'], [12, 'N'], [1, 'E'], [13, 'E'], [5, 'N'], [1, 'E'], [1, 'E'], [7, 'N'], [3, 'W'], [8, 'N']]
	#   board 4: time 161.697s(with prints)
	#       44 steps => [[2, 'N'], [3, 'W'], [5, 'N'], [9, 'W'], [9, 'W'], [9, 'W'], [4, 'N'], [4, 'N'], [6, 'W'], [7, 'N'], [7, 'N'], [17, 'E'], [17, 'E'], [19, 'N'], [21, 'W'], [22, 'W'], [14, 'N'], [13, 'E'], [4, 'N'], [4, 'N'], [9, 'E'], [8, 'E'], [9, 'E'], [8, 'E'], [9, 'E'], [8, 'E'], [9, 'E'], [8, 'E'], [5, 'N'], [3, 'E'], [2, 'N'], [10, 'N'], [10, 'N'], [1, 'W'], [12, 'N'], [12, 'N'], [12, 'N'], [12, 'N'], [15, 'E'], [4, 'N'], [18, 'N'], [20, 'W'], [16, 'N'], [11, 'N']]
	#   board 5: time ?
	#       ? steps => ?
	#   board 6: time
	#
	###
	# determine the cars and their orientation on the grid
	# the dicts for vertical and horizontal cars are necessary to build the board object
	# ones a board is made these dicts are inherited when children are made (self.vertical & self.horizontal)
	orientation = check_cars(chupachup)
	# create starting board
	parent = Board(chupachup, orientation[0], orientation[1])
	# archive the starting board
	archive = dict()
	archive[str(parent.start)] = str(parent.start)
	# create queue, put start board in it
	queue = Queue.Queue()
	queue.put(parent)
	# count the ammount of boards that have been worked through
	counter = 1
	while not queue.empty():
		first = queue.get()
		# create children
		children = first.children()
		winning_board = 0
		won = 0
		# check all the children for victors
		for each in children:
			# if the child is not yet in the archive
			if not str(each.start) in archive:
				# put the child in the archive
				archive[str(each.start)] = str(each.start)
				# loop through the rows in the child grid
				for i in range(parent.height):
					# if the red car is on the current row
					if 1 in each.start[i]:
						# loop over the positions in the row
						for j in range(parent.width):
							# if the position contains the red car
							if each.start[i][j] == 1:
								# set the win condition to 0
								won = 0
							# if the position contains something other than the red car
							elif not each.start[i][j] == 0:
								won += 1
				# if no cars are positioned to the right of the red car won == 0
				if won == 0:
					# return the winning board object
					print "\nwon"
					return each
					break
				# if the red cars path is still blocked
				else:
					if counter % 50000 == 0:
						koffie(each)
					# put the board in the queue
					queue.put(each)
			counter += 1
			# modulo is used properly now
			if counter % 50000 == 0:
				print "counter:", counter/1000000.0, "million", ", queue:", queue.qsize(), ", archive size:", len(archive)
			if queue.empty():
				print "queue is empty"
	print "done"
	#end of while loop & bf algoritme


def df(depth):
	###
	# determine the cars and their orientation on the grid
	# the dicts for vertical and horizontal cars are necessary to build the board object
	# ones a board is made these dicts are inherited when children are made (self.vertical & self.horizontal)
	orientation = check_cars(chupachup)
	# create starting board
	parent = Board(chupachup, orientation[0], orientation[1])
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
			if not str(each.start) in archive and len(each.pathWay) < depth:
				archive[str(each.start)] = len(each.pathWay)
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
					# print "queue", len(stack)
			elif str(each.start) in archive and archive[str(each.start)] > len(each.pathWay):
				archive[str(each.start)] = len(each.pathWay)
				stack.insert(0,each)
			counter += 1
			if counter%10000 == 0:
				print "counter", counter, "stack", len(stack), ", archive size:", len(archive)
			if len(stack) == 0:
				print "help"
		# else:
		# 	break

	#end of while loop

#check a pathway


"""
orientation = check_cars(chupachup)
simulation(100, Board(chupachup, orientation[0], orientation[1]), chupachup)
"""
def astar():


    def heuristics(board):
        cost = 0
        for i in range(board.height):
            if 1 in board.start[i]:
                for j in range(board.width):
                	if board.start[i][j] != 0 and board.start[i][j] != 1:
                		cost += 5
                    	for k in range(board.height):
                    		if board.start[k][j] != 0:
                    			cost += 10


        return cost


    def newheuristics(board):
    	cost = 0
    	# loops over height
    	for i in range(board.height):
    		# found row of red car
    		if 1 in board.start[i]:
    			# loop over width to find coordinates of red car
    			for j in range(board.width):
    				if board.start[i][j] == 1 and board.start[i][j + 1] != 1:
    					for k in range(board.start[i][j], board.width):
    						if board.start[i][k] != 0:
    							cost += 10
    					for n in range(board.start[i][j], board.height):
    						if board.start[j][n] != 0:
    							cost += 10
    					for path in board.pathWay:
    						cost +=2.5
    	return cost
    


    orientation = check_cars(chupachup)
    # initialize the starting board
    boarding = Board(chupachup,orientation[0], orientation[1])
    # create archive/ closed list
    archive_astar = dict()
    archive_astar[str(boarding.start)] = len(boarding.pathWay)
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
        		total = cost_so_far[child] + newheuristics(child)
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



winning_board = astar()
print "done"
runtime = datetime.now() - tijd
print runtime
print len(winning_board.pathWay), winning_board.pathWay
winning_board.pathWay = PathSweep(winning_board.pathWay)
koffie(winning_board)

sim_speed = 10000 / len(winning_board.pathWay)

simulation(0.3, winning_board, chupachup)
