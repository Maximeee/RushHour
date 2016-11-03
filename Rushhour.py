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
		
		