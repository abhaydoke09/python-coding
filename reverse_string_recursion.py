
def reverseString(s,i):
	if i == len(s)-1:
		return s[i]
	else:
		return reverseString(s,i+1) + s[i]

print reverseString('abhay doke',0)