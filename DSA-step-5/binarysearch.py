def binarySearch(arr,low,high,element):

	if high >= low:

		mid = (low+high)//2

		if arr[mid] == element:

			return mid

		elif arr[mid] > element:

			return binarySearch(arr,low,mid-1,element)

		else:

			return binarySearch(arr,mid+1,high,element)

	else:
		return -1

arr = [1,2,3,4,5]

BinarySearch = binarySearch(arr,0,len(arr)-1,4)

if BinarySearch == -1:
	print("element is not present in the array")

else:
	print("element is present at index :-",BinarySearch)