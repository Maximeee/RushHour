''''
Maxime Weekhout, Daniel Jacob, Jobber Bekkers
10669744, 10001228, 10543988
'''

import math
import random
import copy
# import pylab
import numpy
import time
import sys
from msvcrt import getch
# import matlSab

# ([id, position, orientation, length], [etc])
# position = x, y; orientation: nz = 1 ew = 2

chupachups = [
[1,[2,5],2,2],
[2,[1,1],1,2],
[3,[2,1],2,3],
[4,[6,1],1,3],
[5,[4,2],1,3],
[6,[7,2],2,3],
[7,[9,3],1,3],
[8,[1,4],2,2],
[9,[6,4],2,3],
[10,[1,5],1,2],
[11,[4,5],1,2],
[12,[3,6],1,2],
[13,[6,6],2,3],
[14,[9,6],1,3],
[15,[1,7],2,2],
[16,[4,7],1,2],
[17,[5,7],2,2],
[18,[1,8],1,2],
[19,[5,8],1,2],
[20,[2,9],2,2],
[21,[6,9],2,2],
[22,[8,9],2,2]
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
                    print "one"
                    print self.arraynp[x,y+length]
                    # if the position bellow the lowest part is empty
                    if (self.arraynp[x,y+length] == 0):
                        print "two"
                        #change the position of the car on a new board / not changes to old cars "deepcopy"
                        new_cars = copy.deepcopy(cars)
                        # print "cars:", cars[car.id-1].position, "\nnew_cars:", new_cars[car.id].position
                        new_cars[car.id-1].position[1] = car.position[1] + 1
                        # print "cars:", cars[car.id-1].position, "\nnew_cars:", new_cars[car.id].position
                        child = Board(new_cars, self.width, self.height)
                        print numpy.transpose(child.arraynp)
                        child_boards.append(child)
                        counter += 1
                        ### queue new board
                if (y-1 > 0):
                    print "one.2"
                    if (self.arraynp[x,y-1] == 0):
                        print "two.2"
                        new_cars = copy.deepcopy(cars)
                        new_cars[car.id-1].position[1] = car.position[1] - 1
                        child = Board(new_cars, self.width, self.height)
                        print numpy.transpose(child.arraynp)
                        child_boards.append(child)
                        counter += 1
            if (orientation == 2):
                print "EW"

                print x + length, "<", width
                if (x+length < width):
                    print "one.3"
                    print x + length, y
                    print self.arraynp[x+length,y]
                    if (self.arraynp[x+length,y] == 0):
                        print "two.3"
                        new_cars = copy.deepcopy(cars)
                        new_cars[car.id-1].position[0] = car.position[0] + 1
                        child = Board(new_cars, self.width, self.height)
                        print numpy.transpose(child.arraynp)
                        child_boards.append(child)
                        counter += 1
                print x-1, ">", 0
                if (x-1 > 0):
                    print "one.4"
                    if (self.arraynp[x-1,y] == 0):
                        print "two.4"
                        new_cars = copy.deepcopy(cars)
                        new_cars[car.id-1].position[0] = car.position[0] - 1
                        child = Board(new_cars, self.width, self.height)
                        print numpy.transpose(child.arraynp)
                        child_boards.append(child)
                        counter += 1


        print "\n", counter, "children made"
        print "test end"
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

board = Board(cars, 9, 9)
print board.arraynp, "\n"
print board.children()

"""
counter = 0
test = numpy.zeros((6, 6))
test = numpy.transpose(test)
for i in range(0, 6):
    for j in range(0, 6):
        test[i,j] = counter
        counter += 1
print test
print test[0,5]
"""
