A = [1,2,3,2,3,4,1,2,3,4,5,6,7,6,5,3,1,2,3,4]

def Print(A,i):
	if i==len(A):
		return None
	else:
		print A[i]," ",
		Print(A,i+1)
		

print A
Print(A,0)