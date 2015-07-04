## 1 Use convert data to int to catch exception. 
## 2 Add a continue to skip following code
## 3 Just for debug
## I'm sorry. I shouldn't commit the code with comment.
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num) #1
        if (smallest is None) or (largest is None):
            largest = num
            smallest = num
##            print("init")
    except:
        print("Invalid input")
        continue # 2 
    
    if (num < smallest): smallest = num 
    elif (num > largest): largest = num
##    print(largest, smallest) #3

# fail to complete the function to get max and min value.
# 0704


print("Maximum is", largest)
print("Minimum is", smallest)
