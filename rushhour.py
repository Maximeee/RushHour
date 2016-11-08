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
		array = []
		if self.posit[x,y] != 0:
			posarray.append(self.posit[x,y])



		return x,y

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
		














