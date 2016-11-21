''''
Maxime Weekhout, Daniel Jacob, Jobber Bekkers
10669744, 10001228, 10543988
'''
import jobber_vizualize

import math
import random
import copy
import Queue
# import pylab
import numpy
import time
import sys
from msvcrt import getch
# import matlSab

# ([id, position, orientation, length], [etc])
# position = x, y; orientation: nz = 1 ew = 2

chupachups = [
[1,[3,3],2,2],
[2,[3,1],2,2],
[3,[5,1],2,2],
[4,[2,2],2,2],
[5,[4,2],2,2],
[6,[6,2],1,3],
[7,[5,3],1,2],
[8,[1,4],2,2],
[9,[3,4],2,2],
[10,[1,5],1,2],
[11,[4,5],1,2],
[12,[5,5],2,2],
[13,[6,5],2,2]
]

board_size = [6,6]

counter = 0
exit = []


# =================================== #

class Car(object):
    def __init__(self, chupachups):
        self.id = chupachups[0]
        self.orientation = chupachups[2]
        self.length = chupachups[3]
        self.position = chupachups[1]

cars = []
for i in range(0, len(chupachups)):
    car = Car(chupachups[i])
    cars.append(car)

class Board(object):

    def __init__(self, cars, width, height):
        self.width = width
        self.height = height
        self.arraynp = numpy.zeros((width, height))
        self.cars = cars
        self.pathWay = []
        for car in self.cars:
            x = car.position[0] - 1
            y = car.position[1] - 1
            length = car.length
            # 1 == up, 2 == left
            orientation = car.orientation
            # if place is empty
            if self.arraynp[x,y] == 0:
                # put car on board
                self.arraynp[x,y] = car.id
                # if orientation is up/down
                if orientation == 1:
                    # if length is 2
                    if length == 2:
                        # set
						self.arraynp[x, y+1] = car.id
                    elif length == 3:
						self.arraynp[x, y+1] = car.id
						self.arraynp[x, y+2] = car.id
                if orientation == 2:
					if length == 2:
						self.arraynp[x+1, y] = car.id
					elif length == 3:
						self.arraynp[x+1, y] = car.id
						self.arraynp[x+2, y] = car.id
        #self.arraynp = numpy.transpose(self.arraynp)

    def __hash__(self):
        return hash(self.arraynp.tostring())

    def __eq__(self, other):
        if type(other) == numpy.ndarray and type(self) == numpy.ndarray:
            return (self.arraynp == other).all()
        elif (type(other) == str):
            return (self.arraynp.tostring() == other)


    def children(self):
        counter = 0
        child_boards = []
        height = self.height
        width = self.width
        for car in self.cars:
            # y - 1 means move up one on the board
            x = car.position[0] - 1
            y = car.position[1] - 1
            length = car.length
            # 1 == up, 2 == left
            orientation = car.orientation
            numb = car.id
            # move
            # if the car is oriented ns
            if (orientation == 1):
                # if the position bellow? the lowest part of the car is on the board
                if (y+length < height):
                    # if the position bellow the lowest part is empty
                    if (self.arraynp[x,y+length] == 0):
                        #change the position of the car on a new board / not changes to old cars "deepcopy"
                        new_cars = copy.deepcopy(self.cars)
                        new_cars[car.id-1].position[1] = car.position[1] + 1
                        child = Board(new_cars, self.width, self.height)
                        child.pathWay = copy.deepcopy(self.pathWay)
                        child.pathWay.append([car.id, "S"])
                        child_boards.append(child)
                        counter += 1
                        ### queue new board
                # if new position is on the board
                if (y-1 >= 0):
                    # if the new area is empty
                    if (self.arraynp[x,y-1] == 0):
                        new_cars = copy.deepcopy(self.cars)
                        new_cars[car.id-1].position[1] = car.position[1] - 1
                        child = Board(new_cars, self.width, self.height)
                        child.pathWay = copy.deepcopy(self.pathWay)
                        child.pathWay.append([car.id, "N"])
                        child_boards.append(child)
                        counter += 1
            # if orientation is EW
            elif (orientation == 2):
                # if
                if (x+length < width):
                    # if the board to the right is empty
                    if (self.arraynp[x+length,y] == 0):
                        # ensure no changes are made to old cars "deepcopy"
                        new_cars = copy.deepcopy(self.cars)
                        # update position
                        new_cars[car.id-1].position[0] = car.position[0] + 1
                        # create new board
                        child = Board(new_cars, self.width, self.height)
                        # if not winning board append new board
                        child.pathWay = copy.deepcopy(self.pathWay)
                        child.pathWay.append([car.id, "E"])
                        child_boards.append(child)
                        counter += 1
                        # check if won
                        if child.arraynp[self.width-1,y] == 0 and child.arraynp[self.width-2,y] == 1:
                            print "\n\n\n WIN \n\n\n"
                            # return winning identivier and winning board
                            return "win", child_boards
                # if the space to the left is on the board
                if (x-1 >= 0):
                    # if the space to the left is empty
                    if (self.arraynp[x-1,y] == 0):
                        # ensure no changes are made to old cars "deepcopy"
                        new_cars = copy.deepcopy(self.cars)
                        # update position
                        new_cars[car.id-1].position[0] = car.position[0] - 1
                        # append new board
                        child = Board(new_cars, self.width, self.height)
                        child.pathWay = copy.deepcopy(self.pathWay)
                        child.pathWay.append([car.id, "W"])
                        child_boards.append(child)
                        counter += 1

        # return all new boards if non won
        return child_boards

'''
put board 1  in queue
while not won or queue not empty
    take board from queue
    make children
        test if won
    test if child in archive
        put children on queue
        put into archive
    or
        discard
'''
# flip the board to match the orientation in boards.txt
# print numpy.transpose(x.arraynp)

# create starting board
board = Board(cars, board_size[0], board_size[1])
# create archive
archive = dict()
# initialize queue
queue = Queue.Queue()
# archive the start board
archive[hash(board)] = board
# put starting board in queue
queue.put(board)
# store the winning board
winning_board = board

if True:
    # as long as there are boards to try
    while not queue.empty():
        # get the first board from the queue
        board = queue.get()
        # make children from that board
        board_children = board.children()
        # if children() returns the winning identivier
        if board_children[0] == "win":
            # show the winning board
            winning_board = board_children[1][0]
            print "WON"
            print board_children[1][0].pathWay, "\n", numpy.transpose(board_children[1][0].arraynp)
            break
        # if children() returns no winning board
        else:
            # for all the boards children() returned
            for each in board_children:
                # if board is not in archive
                if not hash(each) in archive:
                    # add to archive with board hash as key
                    archive[hash(each)] = each
                    # put board at the end of the queue
                    queue.put(each)

def runSimulation(speed, width, height, board):
    # devine the size of the board
    width = width
    height = height
    # create a starting board
    vizualize = Board(cars, board_size[0], board_size[1])
    # store the winning board + path
    end_board = board
    # store the winning path
    path = end_board.pathWay
    # amount of moves to win
    num = len(end_board.pathWay)
    # ammount of cars that are on the board
    num_cars = len(vizualize.cars)
    # store the path
    path = winning_board.pathWay
    #path = [[3, 'S'], [2, 'W'], [2, 'W'], [7, 'N'], [7, 'N'], [7, 'N'], [7, 'N'], [8, 'W'], [3, 'S'], [3, 'S'], [1, 'W'], [1, 'W'], [1, 'W'], [3, 'N'], [3, 'N'], [5, 'N'], [5, 'N'], [5, 'N'], [6, 'W'], [4, 'S'], [4, 'S'], [8, 'E'], [8, 'E'], [8, 'E'], [3, 'S'], [3, 'S'], [1, 'E'], [7, 'S'], [2, 'W'], [7, 'S'], [7, 'S'], [1, 'W'], [3, 'N'], [3, 'N'], [3, 'N'], [6, 'W'], [6, 'W'], [5, 'S'], [7, 'S'], [6, 'W'], [3, 'S'], [2, 'E'], [2, 'E'], [2, 'E'], [2, 'E'], [3, 'N'], [5, 'N'], [6, 'E'], [6, 'E'], [6, 'E'], [3, 'S'], [3, 'S'], [3, 'S'], [1, 'E'], [7, 'N'], [7, 'N'], [7, 'N'], [7, 'N'], [1, 'W'], [3, 'N'], [3, 'N'], [3, 'N'], [6, 'W'], [6, 'W'], [5, 'S'], [6, 'W'], [3, 'S'], [8, 'W'], [8, 'W'], [5, 'S'], [8, 'W'], [3, 'S'], [9, 'W'], [4, 'S'], [9, 'W'], [9, 'W'], [5, 'S'], [9, 'W'], [3, 'S'], [1, 'E'], [1, 'E'], [1, 'E']]

    # while there are moves left
    anim = jobber_vizualize.RushHourVisualization(vizualize)
    for step in path:
        for car in vizualize.cars:
            if car.id == step[0]:
                if step[1] == 'N':
                    car.position[1] = car.position[1] - 1
                    vizualize = Board(vizualize.cars, width, height)
                elif step[1] == 'S':
                    car.position[1] = car.position[1] + 1
                    vizualize = Board(vizualize.cars, width, height)
                elif step[1] == 'W':
                    car.position[0] = car.position[0] - 1
                    vizualize = Board(vizualize.cars, width, height)
                elif step[1] == 'E':
                    car.position[0] = car.position[0] + 1
                    vizualize = Board(vizualize.cars, width, height)
                anim.update(vizualize)
                ### print step, "\n", numpy.transpose(vizualize.arraynp), "\n\n"
    anim.done()

<<<<<<< HEAD
room = Room(cars, 6, 6)
q.append(room)
print room.arraynp
=======
runSimulation(2, board_size[0], board_size[1], winning_board)

"""
print board.arraynp, "\n"
temp = board.children()
print temp
print "children: ", len(temp)
if temp[0] == "won":
    print "WON"
else:
    for each in temp:
        print numpy.transpose(each.arraynp), "\n"



counter = 0
test = numpy.zeros((6, 6))
test = numpy.transpose(test)
for i in range(0, 6):
    for j in range(0, 6):
        print i, j
        test[i,j] = counter
        counter += 1
print test
print test[0,5]
"""
>>>>>>> f8e3ae81ce113426a565fc6d71d42f4618f870ca
