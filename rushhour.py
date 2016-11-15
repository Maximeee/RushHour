''''
Maxime Weekhout, Daniel Jacob, Jobber Bekkers
10669744, 10001228, 10543988
'''

import math
import random
import pylab
import numpy
import time
import queue

# ([id, position, orientation, length], [etc])
# position = x, y; orientation: nz = 1 ew = 2
chupachups = ([1, [0, 0], 2, 2])
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

		if validmove == True:
			releaseplace(position)

		return new_position

# =================================== #

class Room(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		# 0 is empty, if not 0 car id
		self.posit = numpy.zeros(shape = (width + 1, height))

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
		return self.posit
	
	def archive(self, pos):
		q = queue.Queue()
		if q.full():
			raise ValueError
		
		placeoccupied(pos)
		array = []
		
		for i in self.posit:
			array.append(i)
		q.put(array)
		return q




		q.put(self.posit)
		return q




		 




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

		def move(self, direction, position):
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
				new_position.y = position.yqu
				if validMove(new_position):
					return new_position
			else:
				raise ValueError

	def validmove(self, position):
		if not isoccupied(new_position):
			if car.id == 1 and (new_position == exit):
				return "won"
			elif new_position.x < 0 or new_position.x > room.width or new_position.y < room.0 or new_position.y > room.height:
				return False
			else:
				return True
		else:
			return False



# =================================== #

def runSimulation(chupachups, width, height, exit):
    # anim = RushHour_visualize.RushHourVisualization(chupachups, width, height, exit)
    i = len(chupachups)
    room = room(width, height)
    cars = []
    while i > 0:
        cars.append(car(chupachups))
        i -= 1
    while (car.id == 1 and car.position != exit):
        for entry in cars:
            entry.move()

        start_time = time.time()
        #anim.update(room, robots)
    #anim.done()
    return (time.time() - start_time)

def won(x):
	if x == True:
		anim.done()
		return path


"""
for each in cars
	move up/right
		isvalid? (occupied/boundarycheck)
			not in library?
				update position of car
				update board
					put into library
				break
	move down/left
		isvalid? (occupied/boundarycheck)
			not in library?
				update position of car
				update board
					put into library
				break
