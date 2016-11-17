''''
Maxime Weekhout, Daniel Jacob, Jobber Bekkers
10669744, 10001228, 10543988
'''

import math
import random
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
[4,[6,1],1,3],
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
        self.arraynp = numpy.zeros((width, height))
        for car in cars:
            x = car.position[0] - 1
            y = car.position[1] - 1
            length = car.length
            # 1 == up, 2 == left
            orientation = car.orientation
            print (car.id, ( x, y, ), length, orientation)
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
    def __hash__(self):
        return hash(self.arraynp.toString())

    def __eq__(self, other):
        return (self.arraynp == other.arraynp).all()

    def children(self):
        # move
        if (self.direction == 1):
            print ""

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

board = Board(cars, 6, 6)
board.arraynp = numpy.transpose(board.arraynp)

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
