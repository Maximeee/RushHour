''''
Maxime Weekhout, Daniel Jacob, Jobber Bekkers
10669744, 10001228, 10543988
'''

import math
import random
import copy
import queue
# import pylab
import numpy
import time
import sys
from msvcrt import getch
# import matlSab

# ([id, position, orientation, length], [etc])
# position = x, y; orientation: nz = 1 ew = 2

chupachups = [
[1,[4,3],2,2],
[2,[4,1],2,2],
[3,[3,1],1,3],
[5,[4,4],1,3],
[6,[5,4],2,2],
[7,[1,5],1,2],
[8,[5,6],2,2]
]

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
        for car in cars:
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
        return hash(self.arraynp.toString())

    def __eq__(self, other):
        return (self.arraynp == other.arraynp).all()

    def children(self):
        counter = 0
        child_boards = []
        print "test"
        height = self.height
        width = self.width
        for car in cars:
            print '-', car.id, '-'
            # y - 1 means move up one on the board
            x = car.position[0] - 1
            y = car.position[1] - 1
            length = car.length
            # 1 == up, 2 == left
            orientation = car.orientation
            numb = car.id
            # move
            # if the car is oriented nz
            if (orientation == 1):
                print "NZ"
                # if the position bellow? the lowest part of the car is on the board
                if (y+length < height):
                    # if the position bellow the lowest part is empty
                    if (self.arraynp[x,y+length] == 0):
                        #change the position of the car on a new board / not changes to old cars "deepcopy"
                        new_cars = copy.deepcopy(cars)
                        # print "cars:", cars[car.id-1].position, "\nnew_cars:", new_cars[car.id].position
                        new_cars[car.id-1].position[1] = car.position[1] + 1
                        # print "cars:", cars[car.id-1].position, "\nnew_cars:", new_cars[car.id].position
                        child = Board(new_cars, self.width, self.height)
                        child_boards.append(child)
                        counter += 1
                        ### queue new board
                # if new position is on the board
                if (y-1 >= 0):
                    # if the new area is empty
                    if (self.arraynp[x,y-1] == 0):
                        new_cars = copy.deepcopy(cars)
                        new_cars[car.id-1].position[1] = car.position[1] - 1
                        child = Board(new_cars, self.width, self.height)
                        child_boards.append(child)
                        counter += 1
            # if orientation is EW
            if (orientation == 2):
                # if
                if (x+length < width):
                    # if the board to the right is empty
                    if (self.arraynp[x+length,y] == 0):
                        new_cars = copy.deepcopy(cars)
                        new_cars[car.id-1].position[0] = car.position[0] + 1
                        child = Board(new_cars, self.width, self.height)
                        if car.id == 1 and child.arraynp[self.width-1,y]:
                            print "\nwin\n"
                            child_boards.append(child)
                            return "won", child_boards
                        child_boards.append(child)
                        counter += 1
                if (x-1 >= 0):
                    if (self.arraynp[x-1,y] == 0):
                        new_cars = copy.deepcopy(cars)
                        new_cars[car.id-1].position[0] = car.position[0] - 1
                        child = Board(new_cars, self.width, self.height)
                        child_boards.append(child)
                        counter += 1


        print "\n", counter, "children made"
        print "children end"
        return child_boards
        # if valid
            # return list of children
        # else discard

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

# print numpy.transpose(x.arraynp)
board = Board(cars, 6, 6)
archive = dict()
queue = queue.Queue()
queue.put(board)
do

while not queue.empty():
    board = queue.get()
    board_children = board.children()
    if board_children[0] == "won":
        print "WON"
        break
    else:
        for each in board_children:
            archive[each.hash] = each
            queue.put(each)

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
"""

"""
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
