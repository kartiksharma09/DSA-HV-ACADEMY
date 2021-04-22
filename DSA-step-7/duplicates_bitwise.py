a = input()
duplicates = ""

for i in range(len(a)-1):
	for j in range(i+1,len(a)):
		if a[i] in duplicates:
			break
		elif (ord(a[i])^ord(a[j]))==0:
			if a[j] not in duplicates:
				duplicates=duplicates+" "+a[j]
			
print("duplicates are",duplicates)
