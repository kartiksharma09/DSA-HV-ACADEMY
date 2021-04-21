def isBalanced(brackets):
	stack = []
	brackets = input()

	for i in brackets:
		if i in ["(","[","{"]:
			stack.append(i)
		else:
			if len(stack)==0:
				return False
			else:
				last_ele = stack.pop()

			if last_ele == "(" and i!=")":
				return False
			if last_ele == "[" and i!="]":
				return False
			if last_ele == "{" and i!="}":
				return False

	if len(stack)>0:
		return False
	return True

	if isBalanced(brackets):
		print("Brackets are Balanced")
	else:
		print("Brackets aren't Balanced")
isBalanced(brackets)
