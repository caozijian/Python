with open('james.txt') as jaf:
    data=jaf.readline()

james=data.strip().split(',')

with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as saf:
    data=saf.readline()
sarah = data.strip().split(',')

print(james)
print(julie)
print(mikey)
print(sarah)

print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins,secs) = time_string.split(splitter)
    return(mins+'.'+secs)
clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []
for each_item in james:
    clean_james.append(sanitize(each_item))
for each_item in julie:
    clean_julie.append(sanitize(each_item))
for each_item in mikey:
    clean_mikey.append(sanitize(each_item))
for each_item in sarah:
    clean_sarah.append(sanitize(each_item))

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))

unique_james = []
for each_t in james:
    if each_t not in unique_james:
        unique_james.append(each_t)
print(unique_james[0:3])

unique_julie = []
for each_t in julie:
    if each_t not in unique_julie:
        unique_julie.append(each_t)
print(unique_julie[0:3])

unique_mikey = []
for each_t in mikey:
    if each_t not in unique_mikey:
        unique_mikey.append(each_t)
print(unique_mikey[0:3])

unique_sarah = []
for each_t in sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)
print(unique_sarah[0:3])
