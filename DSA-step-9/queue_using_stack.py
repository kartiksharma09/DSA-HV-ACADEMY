class queue:

	def __init__(self):
		self.f_half = []
		self.s_half = []

	def push(self,val):
		self.f_half.append(val)

	def pop(self):

		if len(self.f_half)==0 and len(self.s_half)==0:
			return "queue is empty"

		elif len(self.f_half)>0 and len(self.s_half)==0:

			while self.f_half:
				value = self.f_half.pop()
				self.s_half.append(value)
			return self.s_half.pop()
		else:

			return self.s_half.pop()

a = queue()

a.push(1)
a.push(2)
a.push(3)
print(a.pop())