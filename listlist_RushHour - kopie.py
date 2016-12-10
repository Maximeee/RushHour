"""
path1 = [[1, "s"], [2, "w"]]
path2 = path1[:]
path2.append([3, "E"])
path3 = path2[:]
path3.append([4, "N"])
print path1, "\n", path2, "\n", path3
"""
import Listlist_Breadth_first_vizualize
import Queue

# imput is in de vorm [[row1],[row1],[row3],[row4], etc]
chupachup = [
[0,0,3,2,2,4],
[0,0,3,0,0,4],
[0,0,3,1,1,4],
[0,0,0,5,6,6],
[7,8,8,5,0,0],
[7,0,0,5,9,9]
]

# board[row][colom]

# accepteerd een grid en print het
def koffie(z):
    for i in range(len(z.start)):
        print z.start[i]
####
# work in progress
def move(car, board, pathWay, x, y, ofset, step):
    new_board = board[:]
    new_board[x - ofset] = board[x - ofset][:]
    new_board[x - ofset][y] = 0
    new_board[x+1] = board[x+1][:]
    new_board[x+1][y] = board[x][y]
    temp = Board(new_board)
    temp.pathWay = pathWay[:]
    temp.pathWay.append([board[x][y], step])
    return temp
####

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
                            # create an array sharing the old grid
                            new_board = self.start[:]
                            # "deepcopy" the row the car is moving into
                            new_board[i+1] = self.start[i+1][:]
                            # set the position in the new row to the car id
                            new_board[i+1][j] = self.start[i][j]
                            # "deepcopy" the row where the other end of the car is
                            new_board[i - empty] = self.start[i - empty][:]
                            # set the position the car used to be to 0
                            new_board[i - empty][j] = 0
                            # create a new board
                            temp = Board(new_board, self.vertical, self.horizontal)
                            # "deepcopy" an array, revering to the parent pathWay
                            temp.pathWay = self.pathWay[:]
                            # append the new step
                            temp.pathWay.append([self.start[i][j], "N"])
                            # append the new board to the children list
                            new_boards.append(temp)
                            ####
                            # all of the above might fit in one function for moving vertical
                            # a similar on could be deficed for horizontal movement
                            # print self.start[i][j]
                            # new_boards.append(move(self.start[i][j], self.start, self.pathWay, empty, i, j, "S"))
                    if i > 0:
                        # UP
                        # Works the same as the move down
                        if self.start[i-1][j] == 0:
                            new_board = self.start[:]
                            new_board[i + empty] = self.start[i + empty][:]
                            new_board[i + empty][j] = 0
                            new_board[i-1] = self.start[i-1][:]
                            new_board[i-1][j] = self.start[i][j]
                            temp = Board(new_board, self.vertical, self.horizontal)
                            temp.pathWay = self.pathWay[:]
                            temp.pathWay.append([self.start[i][j], "N"])
                            new_boards.append(temp)
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
                            # create an array sharing the old grid
                            new_board = self.start[:]
                            # "deepcopy" the row the car is on
                            new_board[i] = self.start[i][:]
                            # set the position the the right of the car to the car id
                            new_board[i][j + 1] = self.start[i][j]
                            # set the left most part of the car to 0
                            new_board[i][j - empty] = 0
                            # create a new grid
                            temp = Board(new_board, self.vertical, self.horizontal)
                            # create an array sharing the parent pathWay
                            temp.pathWay = self.pathWay[:]
                            # append the new step
                            temp.pathWay.append([self.start[i][j], "E"])
                            # append the new board to the children list
                            new_boards.append(temp)
                    if j > 0:
                        # LEFT
                        # works the same as the move right
                        if self.start[i][j-1] == 0:
                            new_board = self.start[:]
                            new_board[i] = self.start[i][:]
                            new_board[i][j-1] = self.start[i][j]
                            new_board[i][j + empty] = 0
                            temp = Board(new_board, self.vertical, self.horizontal)
                            temp.pathWay = self.pathWay[:]
                            temp.pathWay.append([self.start[i][j], "W"])
                            new_boards.append(temp)
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
                # if the red cars path is still blocked
                else:
                    # put the board in the queue
                    queue.put(each)
            counter += 1
            # modulo is used properly now
            if counter % 1 == 0:
                print "counter:", counter, ", queue:", queue.qsize(), ", archive size:", len(archive)
            if queue.empty():
                print "queue is empty"
    print "done"
    #end of while loop & bf algoritme

# simulation(2, Board(chupachup).pathWay, chupachup)
winning_board = bf()
print len(winning_board.pathWay), "\n", winning_board.pathWay
koffie(winning_board)
