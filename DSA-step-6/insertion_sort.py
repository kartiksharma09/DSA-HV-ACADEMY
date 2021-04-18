def insertionSort(arr):
    for i in range(1, len(arr)):

        initial = arr[i]

        j = i-1
        while j >= 0 and initial < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = initial

arr = [1, 11, 3, 5, 6]
insertionSort(arr)
