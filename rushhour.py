''''
Maxime Weekhout, Daniel Jacob, Jobber Bekkers
10669744, 10001228, 10543988
'''
<<<<<<< HEAD
=======

>>>>>>> e31dc118b4f4e1359cd25357eee1427cb8499e8d

import math
import random
import pylab
import numpy

# ([id, position, orientation, length], [etc])
chupachups = ([1, [0, 0], Z, 2])
int counter = 0
exit = []

class Position(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def move(self, direction, position):
		if direction == N:
			new_position.y = position.y + 1
			position.x = position.x
		elif direction == S:
			new_position.y = position.y - 1
			new_position.x = position.x
		elif direction == W:
			new_position.x = position.x - 1
			new_position.y = position.y
		elif direction == E:
			new_position.x = position.x + 1
			new_position.y = position.y
		else:
			raise ValueError

		boundarycheck(new_position)
		positioncheck(new_position)
		return new_position

# =================================== #

class room(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		# 0 is empty, if not 0 car id
		self.posit = numpy.zeros(shape = (width, height))

	def getposition(self, pos):
		x = []
		y = []
		x = pos.getX()
		y = pos.getY()
		array = []
		if self.posit[x,y] != 0:
			posarray.append(self.posit[x,y])
		return x,y

	def isoccupied(self, x, y):
		if (x, y) in self.pos:
			return True
		else:
			return False

	def placeoccupied(self, pos):
		x = pos.getX()
		y = pos.getY()
		self.posit[x,y] = 1

	def releaseplace(self,pos):
		x = post.getX()
		y = pos.getY()
		self.posit[x,y] = 0
'''
	def exit (height, width):
if
			gap = height/2
			exit = bullshit
'''

# =================================== #

class car(object):
	#orientation is NS, EW
	def __init__(self, chupachups):
		self.lenght = lenght
		self.position = position
		self.orientation = orientation

	def getId(self):
		int total_cars = len(chupachups)
		int id = 0
		for i in range(0, total_cars):
			id +=1
			i +=1

	def positioncheck(self, position):
		if isoccupied(new_position):
			invalidmove()

	def boundarycheck(self, position, room):
		if new_position.x < room.x or new_position.x > room.x or new_position.y < room.y or new_position.y > room.y:
			invalidmove()

	def invalidmove():
		raise ValueError

# =================================== #


def runSimulation(chupachups, width, height, exit):
    width = width
    height = height
    num = num_trials
    totaltime = 0
    while num > 0:
#        anim = rushhour_visualize.RushHourVisualization(chupachups, width, height, exit)
        i = len(chupachups)
        room = room(width, height)
        cars = []
        while i > 0:
            cars.append(car(chupachups))
            i -= 1
		'''
        while simulation is not done
            for robot in robots:
                robot.updatePositionAndClean()
            totaltime += 1
#            anim.update(room, robots)
		'''
        num -= 1
#        anim.done()
    return (totaltime/num_trials)
