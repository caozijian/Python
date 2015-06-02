data = open('sketch.txt')
for each_line in data:
    # This version for find :
    '''
    if not each_line.find(':') == -1:
        (role,line_spoken) = each_line.split(':',1)
        print(role,end='')
        print(' said: ',end='')
        print(line_spoken,end='')
        print(each_line,end='')
    '''
    try:
        (role,line_spoken) = each_line.split(':',1)
        print(role,end='')
        print(' said: ',end='')
        print(line_spoken,end='')
        print(each_line,end='')
    except:
        pass
data.close()
