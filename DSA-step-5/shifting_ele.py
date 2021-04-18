arr = [1,2,3,4,5]
m = int(input())
m%=len(arr)

for i in range(len(arr)//2):
	arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]

arr = arr[m:]+arr[:m]
print(arr)