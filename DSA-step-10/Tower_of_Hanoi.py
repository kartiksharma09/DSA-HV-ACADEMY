def towerOfHanoi(n,source,destination,auxiliary):
	if n==1:
		print("move disc 1 from source",source,"to destination",destination)
		return
	towerOfHanoi(n-1,source,auxiliary,destination)

	print("move disc",n,"from source",source,"to destination",destination)

	towerOfHanoi(n-1,auxiliary,destination,source)

towerOfHanoi(4,'a','c','b')