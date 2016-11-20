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

class Room(object):

	def __init__(self, cars, width, height):
		self.arraynp = numpy.zeros((width, height))
		for car in cars:
			x = car.position[0] - 1
			y = car.position[1] - 1
			length = car.length
			orientation = car.orientation
			if self.arraynp[x,y] == 0:
				self.arraynp[x,y] = car.id
				if orientation == 1:
					if length == 2:
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


room = Room(cars, 6, 6)
q.append(room)
print room.arraynp
