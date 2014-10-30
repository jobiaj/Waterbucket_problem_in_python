import string, sys
class manager:
	def __init__ (self) :
		self.queue = []
		self.seen = {}
	def getState (self) :
		if not self.queue : return None
		state = self.queue[0]
		self.queue = self.queue[1:]
		return state
	def addState (self, parentState, newState) :
		if self.seen.has_key(str(newState)) : return
		self.seen[str(newState)] = str(parentState)
		self.queue.append (newState)
	def getSolution (self) :
		solution = []
		state = self.queue[-1]
		while state :
			solution.append (str(state))
			state = self.getParent(state)
		solution.reverse()
		return solution
	def getParent (self, childState) :
		try: return self.seen[str(childState)]
		except : return None
class bucketPlayer :
	def __init__ (self, manager) :
		self.manager = manager
	def test (self, oldstate, newstate) :
		[newA, newB] = newstate
		won = (newA == self.goal or newB == self.goal)
		self.manager.addState (oldstate, newstate)
		return won
	def playGame (self, aMax, bMax, goal) :

		self.goal = goal
		self.manager.addState("", [0,0])
		while 1 :
			oldstate = self.manager.getState()
			[aHas,bHas] = oldstate
			if self.test (oldstate, [aMax,bHas]): break #fill A from well
			if self.test (oldstate, [0,bHas]): break # empty A to well
			if self.test (oldstate, [aHas,bMax]): break # fill B from well
			if self.test (oldstate, [aHas,0]): break # empty B to well
			howmuch = min(aHas, bMax-bHas)
			if self.test (oldstate, [aHas-howmuch,bHas+howmuch]): break # pour A to B
			howmuch = min(bHas, aMax-aHas)
			if self.test (oldstate, [aHas+howmuch,bHas-howmuch]): break # pour B to A
		print "Solution is "
		print string.join (self.manager.getSolution(), "\n")
