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
# position = y, x; orientation: nz = 1 ew = 2

chupachups = ([1, [2, 0], 2, 3], [2, [0,2], 1, 3])

counter = 0
exit = []

# class Position(object):
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
# 	def getX(self):
# 		return self.x
# 	def getY(self):
# 		return self.y


# =================================== #

class Room(object):

	def initroom(self, width, height):
		arraynp = numpy.zeros((width, height))

		i = 0
		for j in chupachups[i][1]:
			a = chupachups[i][1][0]
			b = chupachups[i][1][1]
			if arraynp[a, b] == 0:
				arraynp[a,b] = chupachups[i][0]
				if chupachups[i][2] == 1:
					if chupachups[i][3] == 2:
							arraynp[a+1, b] = chupachups[i][0]
					else:
						arraynp[a+1, b] = chupachups[i][0]
						arraynp[a+2, b] = chupachups[i][0]
				else:
					if chupachups[i][3] == 2:
						arraynp[a, b+1] = chupachups[i][0]
					else:
						arraynp[a, b+1] = chupachups[i][0]
						arraynp[a, b+1] = chupachups[i][0]				
				i +=1

		return arraynp

	# def getposition(self, pos):
	# 	x = pos.getX()
	# 	y = pos.getY()
	# 	array = []
	# 	if self.posit[x,y] != 0:
	# 		posarray.append(self.posit[x,y])
	# 	return x,y

	# def isoccupied(self, board):
	# 	if :
	# 		return True
	# 	else:
	# 		return False

	# def releaseplace(self,pos):
	# 	x = post.getX()
	# 	y = pos.getY()
	# 	self.posit[x,y] = 0

	# def exit (height, width):
	# 	if (height % 2):
	# 		return height/2
	# 	else:
	# 		return (height/2 + 1)

# =================================== #

# class Car(object):

	# def moveUp(self, id, board):
		

		# if direction == 'N':
		# 	new_position[x][y] = position[x][y+1]
		# 	print new_position[x][y]
		# 	if validMove(new_position):
		# 		return new_position[x][y]
		# elif direction == 'S':
		# 	new_position.y = position.y - 1
		# 	new_position.x = position.x
		# 	if validMove(new_position):
		# 		return new_position
		# elif direction == 'W':
		# 	new_position.x = position.x - 1
		# 	new_position.y = position.y
		# 	if validMove(new_position):
		# 		return new_position
		# elif direction == 'E':
		# 	new_position.x = position.x + 1
		# 	new_position.y = position.y
		# 	if validMove(new_position):
		# 		return new_position
		# else:
		# 	raise ValueError

		# if validmove == True:
		# 	releaseplace(position)

		# return new_position

	# def validmove(self, position):
	# 	if not isoccupied(new_position):
	# 		if car.id == 1 and (new_position == exit):
	# 			return "won"
	# 		elif new_position.x < 0 or new_position.x > room.width or new_position.y < 0 or new_position.y > room.height:
	# 			return False
	# 		else:
	# 			return True
	# 	else:
	# 		return False



def RushHour(width, height):
	board = Room().initroom(width, height)
	print board

	while(True):
		maxchup = len(chupachups)
		key = int(raw_input("Give car ID: ")) -1

		while key < 0 or key >= maxchup:
			key = int(raw_input("Try again: ")) -1
		
		move = raw_input("ASDW? ")

		while not (move == 'a' or move == 'A' or move == 'S' or move == 's' or move == 'W' or move == 'w' or move == 'd' or move == 'D'):
			raw_input("Try again: ")
		
		# zorgen dat autos niet botsen
		# zorgen dat het spel gewonnen kan worden
		# [1, [0,3], 2, 3]
		# [2, [0,2], 1, 3]
		
		if move == 'A' or move == 'a':
			if not chupachups[key][2] == 1:
				if not chupachups[key][1][1] -1 < 0:
					b = chupachups[key][1][1] -1
					a = chupachups[key][1][0]
					if board[a][b] == 0:
						chupachups[key][1][1] = chupachups[key][1][1] -1
						chupachups[key][1][0] = chupachups[key][1][0]
		elif move == 'D' or move == 'd':
			if not chupachups[key][2] == 1: 
				if not chupachups[key][1][1] +1 >= height:
					b = chupachups[key][1][1] +1
					a = chupachups[key][1][0]
					# if board[a+(chupachups[key][3])][b] == 0 and board[a+(chupachups[key][3]-1)][b] == 0 :
					chupachups[key][1][1] = chupachups[key][1][1] +1
					chupachups[key][1][0] = chupachups[key][1][0] 

		elif move == 'S' or move == 's':
			if not chupachups[key][2] == 2:
				print "jeej" 
				if not chupachups[key][1][0] + 1 >= width:
					b = chupachups[key][1][1] +1
					a = chupachups[key][1][0] 
					print a, b, board[a][b]
					# if board[a][b] == 0:
					chupachups[key][1][1] = chupachups[key][1][1] 
					chupachups[key][1][0] = chupachups[key][1][0] +1
		
		elif move == 'W' or move == 'w':
			if not chupachups[key][2] == 2: 
				if not chupachups[key][1][0] -1 < 0:
					b = chupachups[key][1][1] 
					a = chupachups[key][1][0] -1
					# if board[a][b] == 0:
					chupachups[key][1][1] = chupachups[key][1][1] 
					chupachups[key][1][0] = chupachups[key][1][0] -1
		
		board = Room().initroom(width, height)
		print board






x=RushHour(5,5)

