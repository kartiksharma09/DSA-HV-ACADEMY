arr =[1,2,4,5,7,8,9]
miss = []

for i in range(1,max(arr)):
	if i not in arr:
		miss.append(i)
	else:
		continue

print(miss)