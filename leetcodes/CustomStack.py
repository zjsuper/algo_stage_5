## customised stack


class CustomStack:
	def __init__(self,maxSize:int):
		self.maxSize = maxSize
		self.stack = [0 for _ in range(maxSize)]
		self.stack_point = -1

	def push(self,x:int):
		if self.stack_point < self.maxSize:
			self.stack_point += 1
			self.stack[self.stack_point] = x

	def pop(self):
		s
		self.stack
