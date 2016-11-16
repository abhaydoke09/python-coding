def checkPalindrome(s):

	if len(s) == 2:
		if s[0] == s[1]:
			return True
	if s == None:
		return True
	if s[0] != s[-1]:
		return False
	elif len(s) == 1:
		return True
	else:
		return True and checkPalindrome(s[1:-1])

print checkPalindrome("bhsfhb")