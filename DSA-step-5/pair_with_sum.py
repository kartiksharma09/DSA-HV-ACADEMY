arr = [1,2,3,4,5,6,7]
pair = []
sum1 = 10
flag = False
for i in range(0,(len(arr))):
	flag = False
	for j in range(i+1,(len(arr))):
		if arr[i]+arr[j]==sum1:
			print(arr[i],arr[j])
			flag = True
			break
	if flag == True:
		break
				
