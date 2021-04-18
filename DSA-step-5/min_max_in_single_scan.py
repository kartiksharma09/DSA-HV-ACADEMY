a = [1,-1,2,-6,3]
max1 = a[0]
min1 = a[0]
for i in range (len(a)):
	if a[i]<min1:
		min1 = a[i]
	if a[i]> max1:
		max1 = a[i]
print(" maximum is :-",max1 ,"\n","minimum is :-",min1)