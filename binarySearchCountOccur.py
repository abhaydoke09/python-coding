def findFirst( A, B):
        A = list(A)
        low = 0
        high = len(A)-1
        lowIndex = -1
        while(low<=high):
            mid = int(low+(high-low)/2)
            if A[mid] == B:
                lowIndex = mid
                high = mid - 1
            elif A[mid]>B:
                high = mid-1
            else:
                low = mid+1
        return lowIndex
    
def findLast( A, B):
    A = list(A)
    low = 0
    high = len(A)-1
    highIndex = -1
    while(low<=high):
        mid = int(low+(high-low)/2)
        if A[mid] == B:
            highIndex = mid
            low = mid + 1
        elif A[mid]>B:
            high = mid-1
        else:
            low = mid+1
    return highIndex

def findCount( A, B):
    low = findFirst(A,B)
    last = findLast(A,B)
    if low == -1 or last == -1:
        return 0
    else:
        return last-low
        
        
A = [ 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 10 ]
B = 1

print findCount(A,B)+1