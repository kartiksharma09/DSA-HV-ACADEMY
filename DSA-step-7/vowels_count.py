a = "kartik".lower()
vowels = 0
consonants = 0
li = ["a","e","i","o","u"]
for i in a:
	if i in li :
		vowels+=1
print("vowels:-",vowels)
print("consonants:-",len(a)-vowels)