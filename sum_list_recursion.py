A = [1,3,5,7,9]

s = 0 
def sum_list(l):
	if len(l)==1:
		return l[0]
	else:
		return l[0] + sum_list(l[1:])


print sum_list(A)

