A = [1,3,2,4,7,5,8,6,9]
for i in range(len(A)):

    key = i
    for j in range(i+1, len(A)):
        if A[key] > A[j]:
            key = j

    A[i], A[key] = A[key], A[i]
print ("Sorted array")
