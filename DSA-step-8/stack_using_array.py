class Mystack:

	def __init__(self):

		self.stack = []

	def isempty(self):

		return len(self.stack)==0

	def push(self,data):

		self.stack.append(data)

	def pop(self):

		if len(self.stack)!=0:

			self.stack.pop()

		else:

			print("stack is empty")

	def peek(self):

		if len(self.stack)!=0:

			return self.stack[-1]

		else:

			print("stack is empty")


	def show(self):

		print(self.stack)

	def length(self):

		return len(self.stack)

stack_op = Mystack()

stack_op.push(1)
stack_op.show()
stack_op.push(2)
stack_op.show()
stack_op.peek()