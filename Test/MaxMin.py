
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    if smallest is None:
        largest = num
        smallest = num
##        print("Oh!No!")
##        
##    try:
####        if (type(num) == int) and (largest == None):
####            largest = num
####            smallest = num
####
##
##    except:
##        print("Invalid input")

# fail to complete the function to get max and min value.
# 0704
    if (num > largest):
        largest = num
    elif (num < smallest):
        smallest = num        
    print(largest, smallest)

print("Maximum", largest)
print("Minimum", smallest)
