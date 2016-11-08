def prettyPrint(A):
    for i in range(1,A+(A-1)+1):
        for j in range(1,A+(A-1)+1):
            print max(A-(i-1),A-(A+(A-1) -j),A-(j-1),A-(A+(A-1)-i)),
        print
    
prettyPrint(3)
            
        