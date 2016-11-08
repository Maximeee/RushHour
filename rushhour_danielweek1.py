import math
import random

import pylab
import numpy



class room(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.posit = numpy.zeros(shape = (x, y))

	def getposition(self, pos):
		x = []
		y = []
		x = pos.getX()
		y = pos.getY()

		self.pos = [x,y]
		











