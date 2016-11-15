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
# import matlSab

# ([id, position, orientation, length], [etc])
# position = x, y; orientation: nz = 1 ew = 2

chupachups = ([1, [0, 3], 2, 3], [2, [0,2], 1, 2])
counter = 0
exit = []

class Position(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def getX(self):
		return self.x
	def getY(self):
		return self.y


# =================================== #

class Room(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		# 0 is empty, if not 0 car id

		arraynp = numpy.zeros((width, height))

		i = 0
		for j in chupachups[i][1]:
			a = chupachups[i][1][0]
			b = chupachups[i][1][1]
			if arraynp[a, b] == 0:
				arraynp[a,b] = chupachups[i][0]
				if chupachups[i][2] == 1:
					arraynp[a+1, b] = chupachups[i][0]
				else:
					arraynp[a, b+1] = chupachups[i][0]
				i +=1	

		print arraynp

	def getposition(self, pos):
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

	def releaseplace(self,pos):
		x = post.getX()
		y = pos.getY()
		self.posit[x,y] = 0

	def exit (height, width):
		if (height % 2):
			return height/2
		else:
			return (height/2 + 1)

# =================================== #

class Car(object):
	#orientation is NS, EW
	def __init__(self, chupachups):
		self.id = chupachups[0]
		self.position = chupachups[1]
		self.orientation = chupachups[2]
		self.lenght = chupachups[3]

	def move(self, id, direction):

		if direction == 'N':
			new_position.y = position.y + 1
			new_position.x = position.x
			if validMove(new_position):
				return new_position
		elif direction == 'S':
			new_position.y = position.y - 1
			new_position.x = position.x
			if validMove(new_position):
				return new_position
		elif direction == 'W':
			new_position.x = position.x - 1
			new_position.y = position.y
			if validMove(new_position):
				return new_position
		elif direction == 'E':
			new_position.x = position.x + 1
			new_position.y = position.y
			if validMove(new_position):
				return new_position
		else:
			raise ValueError

		if validmove == True:
			releaseplace(position)

		return new_position

	def validmove(self, position):
		if not isoccupied(new_position):
			if car.id == 1 and (new_position == exit):
				return "won"
			elif new_position.x < 0 or new_position.x > room.width or new_position.y < 0 or new_position.y > room.height:
				return False
			else:
				return True
		else:
			return False

x = Room(5,5)