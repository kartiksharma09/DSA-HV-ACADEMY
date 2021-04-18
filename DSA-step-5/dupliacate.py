
a = [1,3,2,1]

dict1={}
for i in a:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1
fake=[]
for j in dict1:
    if dict1[j]>1:
        fake.append(j)
if len(fake)==0:
    print("No duplicates found in this ARRAY")
else: 
    print(fake)
