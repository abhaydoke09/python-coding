class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        B = map(int, A.strip())
        B = map(lambda x:0 if x== 1 else 1,B)
        print A
        max_sofar = 0
        max_before = 0
        L = -1
        R = -1
        L =[]
        for i in range(len(B)):
            max_before = max(0, max_before + B[i])
            if max_before == 0:
                L.append(i) 
            if max_before > max_sofar:
                max_sofar = max_before
                R=i
        if R == -1:
            return []
        l = 0
        for l in range(len(L)):
            if L[l]>R:
                break
        l+=1
        return([l,R])
A = '010'


s = Solution()
print s.flip(A)