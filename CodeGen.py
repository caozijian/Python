fin = open('start.txt','r')
data = fin.read()
data = data.strip('\n')
data = data.split('\t')
data_op = []
for each_item in data:
    data_op.append(int(each_item))
