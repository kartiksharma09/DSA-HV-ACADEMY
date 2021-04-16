arr = [5,4,3,2,1,6]

def quickSort(arr):

	if len(arr) <= 1:

		return arr

	else:

		pivot = arr.pop()

	greater_than_pivot = []
	lower_than_pivot = []

	for i in arr:
		if i > pivot:
			greater_than_pivot.append(i)

		else:
			lower_than_pivot.append(i)


	return quickSort(lower_than_pivot)+[pivot]+quickSort(greater_than_pivot)

print(quickSort(arr))