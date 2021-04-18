def linearSearch(arr,element):

	for i in arr:
		if arr[i]==element:
			return "the element is present at index :-",i

	return -1

arr=[1,3,4,5,6]
print(linearSearch(arr,5))
