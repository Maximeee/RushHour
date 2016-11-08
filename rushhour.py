
import math
import random

import pylab
import numpy

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
		
class car:
	#orientation is NS, EW
	def __init__(self, lenght, position, orientation)
		self.lenght = lenght
		self.position = position
		self.orientation = orientation

	def move(self, direction):

		if direction == N:
			position.y += 1
		elif direction == S:
			position.y -= 1
		elif direction == W:
			position.x -= 1
		elif direction == E:
			position.x += 1
		else:
			raise ValueError

	def postionabsolute(self):









