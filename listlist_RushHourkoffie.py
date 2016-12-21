"""
path1 = [[1, "s"], [2, "w"]]
path2 = path1[:]
path2.append([3, "E"])
path3 = path2[:]
path3.append([4, "N"])
print path1, "\n", path2, "\n", path3
"""
import Queue

# imput is in de vorm [[row1],[row1],[row3],[row4], etc]


chupachup = [
[ 2, 2, 2, 3, 0, 4, 5, 0, 0],
[ 0, 0, 0, 3, 0, 4, 5, 6, 6],
[ 0, 0, 0, 3, 7, 7, 8, 0, 0],
[ 0, 0, 0, 0, 9, 9, 8,10,10],
[ 0, 0,11,11,11,12, 1, 1,13],
[14, 0,15, 0, 0,12, 0, 0,13],
[14, 0,15,16,16,12,17,17,13],
[18,19,20,20,21,22,22,22,23],
[18,19,24,24,21, 0, 0, 0,23]
]



# board[row][colom]

# accepteerd een grid en print het
def koffie(z):
    print "steps:", len(z.pathWay), ", path:", z.pathWay
    for i in range(len(z.start)):
        row = str(z.start[i])
        row.replace(" ", "")
        print z.start[i]
    print "\n"


def moveVert(board, i, j, k, empty, ori):
    new_board = board.start[:]
    new_board[i+k] = board.start[i+k][:]
    new_board[i+k][j] = board.start[i][j]
    new_board[i - empty] = board.start[i - empty][:]
    new_board[i - empty][j] = 0
    temp = Board(new_board, board.vertical, board.horizontal)
    temp.pathWay = board.pathWay[:]
    temp.pathWay.append([board.start[i][j], ori])
    return temp

def moveHor(board, i, j, k, empty, ori):
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
                    empty = self.vertical[self.start[i][j]] - 1
                    # if the move is valid/ new position is still on the board
                    # -1 as it is 0 indexed
                    if i < self.height - 1:
                        # DOWN
                        # move the car down if possible
                        if self.start[i+1][j] == 0:
                            new_boards.append(moveVert(self, i, j, 1, empty, "S"))
                    if i > 0:
                        # UP
                        # Works the same as the move down
                        if self.start[i-1][j] == 0:
                            new_boards.append(moveVert(self, i, j, -1, -empty, "N"))
                # if the car found is orientated horizontally
                if self.start[i][j] in self.horizontal:
                    # check the length of the car
                    # and thus which position to clear
                    empty = self.horizontal[self.start[i][j]] - 1
                    # if a step right still is within the grid
                    if j + 1 < self.width:
                        # RIGHT
                        # if the position to the right is empty
                        if self.start[i][j+1] == 0:
                            new_boards.append(moveHor(self, i, j, 1, empty, "E"))
                    if j > 0:
                        # LEFT
                        # works the same as the move right
                        if self.start[i][j-1] == 0:
                            new_boards.append(moveHor(self, i, j, -1, -empty, "W"))
        return new_boards

# Work in progress
def simulation(speed, path, chupachup):
    starting_board = Board(chupachup)
    path = [[2, 'W'], [2, 'W'], [3, 'W'], [3, 'W'], [4, 'W'], [5, 'W'], [6, 'N'], [1, 'W'], [7, 'N'], [7, 'N'], [9, 'E'], [9, 'E'], [11, 'N'], [11, 'N'], [12, 'W'], [12, 'W'], [12, 'W'], [11, 'S'], [13, 'W'], [13, 'W'], [13, 'W'], [11, 'S'], [9, 'W'], [6, 'S'], [6, 'S'], [6, 'S']]
    for step in path:
        for i in range(len(starting_board.start)):
            for j in range(len(starting_board.start[0])):
                if not starting_board.start[i][j] == 0:
                    if starting_board.start[i][j] in starting_board.vertical:
                        print "simulation", starting_board.start[i][j]


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
                                # set the win condition to 0
                                ###
                                # using only this elif statement should be the first heuristic for a* as it counts the number of positions taken besides the ones taken by the red car
                                # if you only want to count the cars to the right of the red car take the if statement and the elif statement
                                ###
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
                print "counter:", counter/1000000, "million", ", queue:", queue.qsize(), ", archive size:", len(archive)
            if queue.empty():
                print "queue is empty"
    print "done"
    #end of while loop & bf algoritme
def astar(): 

  
    def heuristics(board):
        cost = 0
        for i in range(0, board.height):
            if 1 in board.start[i]:
                for j in range(0, board.width):
                    if board.start[i][j] != 0 and board.start[i][j] != 1:
                        cost += 10
                        print cost
                        
        return cost

    
    
    orientation = check_cars(chupachup)
    # initialize the starting board
    boarding = Board(chupachup,orientation[0], orientation[1])
    # create archive/ closed list
    archive_astar = dict()
    # create open list 
    priority = Queue.PriorityQueue()
    # put starting board in queue
    priority.put((0, boarding))
    counter = 0
    came_from = {}
    cost_so_far = {}
    came_from[boarding] = 0
    cost_so_far[boarding] = 0
    won = 0
    winning_board = 0
    # until there are no more positions and more nodes to traverse
    while not priority.empty():
        # get first board
        score, boarding = priority.get()
        # make children of that board
        childrens = boarding.children()
        # loops over height of board
        for child in childrens:
            if 1 in child.start:
                for i in range(0, boarding.height):

                    for child in childrens:
                        counter += 1
                        # current costs plus costs of child
                        childCost = cost_so_far[boarding] + 1
                        # check if child is in archive
                        if not child in archive_astar:
                            # set cost of child to childcost
                            cost_so_far[child] = childCost
                            # totalcosts of move
                            total = cost_so_far[child] + heuristics(child)
                            # puts total costs in queue
                            priority.put( (total, child))
                            # sets path
                            came_from[child] = boarding
                            # archive child
                            archive_astar[child] = child
                            #print "counter", counter, "queue", priority.qsize(), ", archive size:", len(archive_astar)

        return came_from, cost_so_far

    simulation(2, Board(chupachup).pathWay, chupachup)
    winning_board = astar()
    print winning_board
    print "steps:", len(winning_board.pathWay), "\n", winning_board.pathWay
    koffie(winning_board)
                    
