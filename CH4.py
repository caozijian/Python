import sys
man = []
other = []
try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':',1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing!')
print(man)
print(other)
                
try:
    man_file = open('man_data.txt','w')
    other_file = open('other_data.txt','w')

    print(man,file=man_file)
    print(other,file=other_file)



except IOError:
    print('File error')
finally:
    man_file.close()
    other_file.close()

try:
    data = open('mising.txt')
    print(data.readline(),end='')
except IOError as err:
    print('File error' + str(err))
finally:
    if 'data' in locals():
        data.close()

def print_lol(the_list,indent = False,level =0,fh=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,fh)
        else:
            for tab_stop in range(level):
                print("\t",end='',file=fh)
            print(each_item,file=fh)
try:
    with open('man_data.txt','w') as man_file, open('other_data','w') as other_file:
        print_lol(man,man_file)
        print_lol(other,other_file)
except IOError as err:
    print('file error '+ str(err))

import pickle
with open('mydata.pickle','wb') as mysavedata:
    pickle.dump([1,2,'three'],mysavedata)
with open('mydata.pickle','rb') as myrestoredata:
    a_list = pickle.load(myrestoredata)
print(a_list)
