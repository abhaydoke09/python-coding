class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        n = len(A)
        print n
        max_ones = A.count('1')
        R = -1
        L = -1
        print type(A)
        for i in range(n):
            for j in range(i,n):
                temp_s = A[:i]
                for k in range(i,j+1):
                    if A[k] == '1':
                        temp_s += '0'
                    else:
                        temp_s += '1'
                temp_s += A[j+1:]
                        
                ones = temp_s.count('1')
                if ones>max_ones:
                    max_ones = ones
                    L = i
                    R = j
        if L == -1 and R == -1:
            return []
        else:
            return [L+1,R+1]
        
A = '1101'
s = Solution()
print s.flip(A)