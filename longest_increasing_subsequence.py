class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        d = {}
        max_length = 0
        for i in range(1,len(A)+1):
            current_value = A[i-1]
            print current_value
            if i == 1:
                max_length = 1
                d[max_length] = [current_value]
            else:
                for j in range(1, max_length+1):
                    if (current_value > d[j][-1]) and (j == max_length):
                        d[max_length+1] = d[max_length]+[current_value]
                        max_length+=1
                    elif (current_value > d[j][-1]) and (current_value < d[j+1][-1]):
                        d[j+1] = d[j]+[current_value]
                    elif current_value < d[j][-1]:
                        if (len(d[j])>1):
                            if (d[j][-2]<current_value):
                                d[j][-1] = current_value
                        else:
                            d[j][-1] = current_value

            print d
                    
        #print d
        #print max_length
        return max_length 


A = [ 69, 54, 19, 51, 16, 54, 64, 89, 72, 40, 31, 43, 1, 11, 82, 65, 75, 67, 25, 98, 31, 77, 55, 88, 85, 76, 35, 101, 44, 74, 29, 94, 72, 39, 20, 24, 23, 66, 16, 95, 5, 17, 54, 89, 93, 10, 7, 88, 68, 10, 11, 22, 25, 50, 18, 59, 79, 87, 7, 49, 26, 96, 27, 19, 67, 35, 50, 10, 6, 48, 38, 28, 66, 94, 60, 27, 76, 4, 43, 66, 14, 8, 78, 72, 21, 56, 34, 90, 89 ]
s = Solution()
print s.lis(A)