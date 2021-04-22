
str1 = input()
permutations = []

def permuteString(string,i,length):

	if i == length:
		permutations.append(" ".join(string))

	else:
		for j in range(i,length):
			string[i],string[j] = string[j],string[i]

			permuteString(string,i+1,length)

			string[i],string[j] = string[j],string[i]

permuteString(list(str1),0,len(str1))
print("permutations are",str(permutations))