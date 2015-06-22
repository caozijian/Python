# This is edit by VIM 
# 2015.6.20 First try to conig in Ubuntu.
import math
fin = open('start.txt','r')
data = fin.read()
fin.close()

data = data.strip('\n')
data = data.split('\t')
data_op = []
for each_item in data:
    data_op.append(each_item)
#print(data)
# data_op is operation raw data.

### Convert to bytearray are not necessary.
### You can just use int(i) to convert a char to a number.
##
##data_op_byte = []
##for each_item in data_op:
##    data_op_byte.append(bytearray(each_item,'utf-8'))
##
###print(data_op_byte)


#Demo code is 912 154 906 728, 991 432 570 015
    
def cs(code):
    i = 0
    j = 0
    A = []
    P = []
    R = []
    Q = []
    temp = 0
    # reverse a string
    code = code[::-1]
    for i in range(8):
        j = 2*i + 1
        A.append(int(code[i]))
        P.append(int(code[i])*j)
        Q.append(math.floor(int(code[i])*j/10))
        R.append(P[i] - 10*Q[i])
        #round(bit_of_code*j/10-math.floor(bit_of_code*j/10),2))
    SQR = sum(Q) + sum(R)
    M = (math.floor(SQR/10)+1)*10 - SQR
    CB = M - 10*math.floor(M/10)
    strCB = str(CB)
    # extend the code
    #code.extend(bytearray(strCB,'utf-8'))
    code=code[::-1]+strCB
    return code
##    print('A is:')
##    print(A)
##    print('P is:')
##    print(P)
##    print('Q is:')
##    print(Q)
##    print('R is:')
##    print(R)
##    #
##    print(SQR)
##    print(M)
##    print(CB)
    
    
#print(data_op_byte[0])

fin = open('dumycode.txt','w')

# dumy code
for each_item in data_op:
    for i in range(1000):
        temp = str(int(each_item)+i)
##        print(cs(temp))
        fin.write(cs(temp)+'\n')
fin.close()
