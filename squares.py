def squareSum(A):
    if A == 0:
        return [[0,0]]
    ans = []
    a = 0
    while a*a<A:
        b = 0
        while b*b<A:
            if a*a + b*b == A:
                ans.append([a,b])
            b+=1
        a+=1
    return ans
    
print squareSum(2)