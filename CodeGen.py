import math
fin = open('start.txt','r')
data = fin.read()
data = data.strip('\n')
data = data.split('\t')
data_op = []
for each_item in data:
    data_op.append(each_item)
print(data)

data_op_byte = []
for each_item in data_op:
    data_op_byte.append(bytearray(each_item,'utf-8'))

print(data_op_byte)



def cs(code):
    i = 0
    j = 0
    P = []
    R = []
    Q = []
    temp = 0

    for bit_of_code in code:
        j = 2*i + 1
        P.append(bit_of_code)
        temp = math.floor(bit_of_code*j/10)
        Q.append(temp)
        R.append(bit_of_code - 10*temp)
        #round(bit_of_code*j/10-math.floor(bit_of_code*j/10),2))
        SQR = sum(Q) + sum(R)
        
        
    print(Q)
    print(R)
    
print(data_op_byte[0])
cs(data_op_byte[0])

        