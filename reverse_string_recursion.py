
def reverseString(s):
	if len(s) == 1:
		return s
	else:
		return reverseString(s[1:]) + s[0]

print reverseString('abhay doke')