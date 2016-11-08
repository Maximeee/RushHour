
import math
import random

import pylab
import numpy

int counter = 0

class room(object):

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.posit = numpy.zeros(shape = (width, height))

	def getposition(self, pos):
		x = []
		y = []
		x = pos.getX()
		y = pos.getY()

		self.pos = [x,y]

	def isoccupied(self, x, y):
		if(x, y) in self.pos:
			return True
		else:
			return False

	def placeoccupied(self, pos):
		x = pos.getX()
		y = pos.getY()
		self.posit[x,y] = 1

	def releaseplace(self,pos)
		x = post.getX()
		y = pos.getY()
		self.posit[x,y] = 0
		
class car(object):
	#orientation is NS, EW
	def __init__(self, lenght, position, orientation)
		self.lenght = lenght
		self.position = position
		self.orientation = orientation

	def move(self, direction, position):
		if direction == N:
			new_position = position.y + 1
		elif direction == S:
			new_position = position.y - 1
		elif direction == W:
			new_position = position - 1
		elif direction == E:
			new_position = position + 1
		else:
			raise ValueError

		positioncheck(new_position)
		boundarycheck(new_position)
		counter++

	def positioncheck(self, ):
		

	def boundarycheck(self, position, room):
		if new_position.x < room.x || new_position.x > room.x || new_position.y < room.y || new_position.y > room.y:
			invalidmove()

	def invalidmove():
		raise ValueError
