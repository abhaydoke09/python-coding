n = 2000

def convertToString(n, base):
	convertString = "0123456789ABCDEF"
	if n<base:
		return convertString[n]
	else:
		return convertToString(n//base,base) + convertString[n%base]

print convertToString(n,16)


def reverseString(s,i):
	if i == len(s)-1:
		return s[i]
	else:
		return reverseString(s,i+1) + s[i]

print reverseString('abhay doke',0)

