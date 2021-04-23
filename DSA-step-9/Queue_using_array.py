class MyQueue:

	def __init__(self):
		self.queue = []

	def isempty(self):
		return len(self.queue)==0

	def push(self,data):

		self.queue.insert(0,data)

	def pop(self):

		if len(self.queue)!=0:

			self.queue.pop()

		else:

			print("queue is empty")

	def peek(self):

		if len(self.queue)!=0:

			return self.queue[-1]

		else:

			print("queue is empty")


	def show(self):

		print(self.queue)

	def length(self):

		return len(self.queue)


Queue_Op = MyQueue()

Queue_Op.push(1)
Queue_Op.show()
Queue_Op.push(2)
Queue_Op.show()
Queue_Op.peek()