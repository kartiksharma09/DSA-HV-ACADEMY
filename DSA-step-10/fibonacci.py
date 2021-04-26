fib_memo = {}
def fibonacci(n):
	if n in fib_memo:
		return fib_memo[n]
	if n<2:
		return n
	elif n>=2:
		fib_value= fibonacci(n-1)+fibonacci(n-2)
	fib_memo[n]=fib_value
	return fib_value	

print(fibonacci(9))