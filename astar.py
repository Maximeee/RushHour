from Queue import PriorityQueue
def child (self, position):
	parent = self.position

def heuristics(a, b):
	  return abs(a.x - b.x) + abs(a.y - b.y)




def astar(start, node, goal):
	# create priority queue
	priority = Queue.PriorityQueue()
	# put starting point onto queue
	priority.put(start)
	# where you came from
	g[start] = None
	# cost so far
	h[start] = 0
	
	while not priority.empty():
		node = priority.get()
		if node == goal:
		return True
	else:
		# want to check children of node
		for next in node.children(node):
			fCost = h[node] + children.cost(node, next)
			if next not in h or fCost < h[next]:
				# proceed
				h[next] = fCost
				# store fcost of that child + score for how close we are to goal
				Priorities = fCost + heuristics(goal, next)
				priority.put(next, priorities)
				g[next] = node
			







