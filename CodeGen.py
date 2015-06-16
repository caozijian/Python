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
    data_op_byte.append(bytearray(each_item,0))
