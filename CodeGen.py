# This is edit by VIM 
# 2015.6.20 First try to conig in Ubuntu.
# Generate the code and target chute no
# 2015-06-24 Revise the comment.
# Todo
# 1 Auto generate the target chute no
# 2 Generate the SQL statements

import math
# Original Data
fin = open('start.txt','r')
data = fin.read()
fin.close()
# clean the data

data = data.strip('\n')
data = data.split('\t')
# data_op is operation raw data.
data_op = []
for each_item in data:
    data_op.append(each_item)

### Convert to bytearray are not necessary.
### You can just use int(i) to convert a char to a number.
##
##data_op_byte = []
##for each_item in data_op:
##    data_op_byte.append(bytearray(each_item,'utf-8'))
##
###print(data_op_byte)


# Demo code are 912 154 906 728, 991 432 570 015

# Compute the check bit and extend the code.    
def cs(code):
    # The index
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
    code = code[::-1] + strCB
    return code
##    just for debug.
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

# Generate dummy Chute no based on dummy code.
def dummyChute(code):
    print(int(code[7:11]))
    
    
# Test code
# The correct results are
##912154906728
##701348355941
##207744475920
##201657318097
##902086211164
##033152369988
##207727165726
##test code
dummyCode = ['91215490672','70134835594','20774447592'
             ,'20165731809','90208621116','03315236998'
             ,'20772716572','43030010000']
##test code
print('----Test code start----')
print('Format:')
print('-Bar code')
print('-Index 7 to 11')
print('\n')
for item in dummyCode:
    print(cs(item))
    dummyChute(item)
print('----Test code end----')
# File output
##fin = open('dumycode.txt','w')
##
### dumy code
##for each_item in data_op:
##    for i in range(1000):
##        temp = str(int(each_item)+i)
####        print(cs(temp))
##        fin.write(cs(temp)+'\n')
##fin.close()
