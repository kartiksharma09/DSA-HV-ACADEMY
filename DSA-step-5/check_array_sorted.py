
arr = [1,2,4,5,6,7]

sorted_arr =0

for i in range(1,len(arr)-1):
	if arr[i] < arr[i-1] or arr[i] > arr[i+1]:
		sorted_arr = -1

	else:
		sorted_arr = 1

if sorted_arr == 1:
	print("array is sorted")
else:
	print("array is not sorted")