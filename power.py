import math
def isPower(A):
        if A == 1:
            return True
        l = []
        
        for i in range(2,int(math.ceil(math.sqrt(A)))+1):
            for j in range(2,31):
                s = i**j
                if s==A:
                    return True
                if i**j>2147483648:
                    break
        return False
                
                
print isPower(1024000000)