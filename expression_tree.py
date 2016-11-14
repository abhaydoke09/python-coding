import sys
import re

while(True):
    input_string = ''   #input_string line will contain every input
    try:
        input_string = raw_input()
    except:
        break
    if len(input_string) == 0:
        pass
    
    input_string = input_string.replace(" ","").replace('\n','')    #replace multiple white spaces with single white space and remove newline character
    
    s = input_string.split('/')     #split the input_string by /
    expression = s[0]
    operations = s[1]
    operations = re.sub( 'S+', 'S', operations )    #replace multiple S with single S, as it does the same operation
    
    for opr in operations:
        print expression
        if opr == 'R':  #reverse the string and replace '(' with ')' and vice-versa 
            new_string = ''
            for i in range(len(expression)-1,-1,-1):
                c = expression[i]
                if c == '(':
                    new_string += ')'
                elif c == ')':
                    new_string += '('
                else:
                    new_string += c
        elif opr == 'S':
            i = 0
            new_string = ''
            flag = False    #flag will turn True as soon as the first parentheses are removed 
            if not expression[i]!= '(':     #if the first character is not a variable
                while(i<len(expression)):
                    if (expression[i] == '(') and not flag:
                        if expression[i+1] != '(':
                            i = i+1
                            while(expression[i]!=')'):
                                new_string+= expression[i]
                                i=i+1
                            flag = True
                        else:
                            i = i+1
                            new_string += expression[i]
                    else:
                        new_string+=expression[i]
                    i = i+1
            else:
                new_string = expression
        expression = new_string
        
    print expression