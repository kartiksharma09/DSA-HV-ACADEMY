a = [1,7,8,6,5,4,3,9,21]  

flag=False

for i in range(1,len(a)+1):

    if flag==True:
        break

    flag=True

    for j in range(len(a)-i):

        if a[j]>a[j+1]:

            a[j],a[j+1]=a[j+1],a[j]
            
            flag=False

print(a)
	