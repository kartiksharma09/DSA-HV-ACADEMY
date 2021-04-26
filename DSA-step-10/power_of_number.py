def exponent(number,power):
	if power == 1:
		return number

	else:
		power = power-1
		return number*exponent(number,power)

print(exponent(5,3))