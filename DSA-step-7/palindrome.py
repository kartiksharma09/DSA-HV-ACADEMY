string = "nayana"
rev_string = ""
for i in string[::-1]:
	rev_string+=i

if string == rev_string:
	print("Palindrome")
else:
	print("not Palindrome")