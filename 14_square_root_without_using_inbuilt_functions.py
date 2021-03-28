""" Design a Python Script to determine the Square Root of a given number without using inbuilt functions in Python."""
a = input("Enter the number: ")
ob = list(a)
count = ob.count("0")
if len(a) % 2 != 0:
    c = "0"+a
else:
    c = a
list1 = []


for i in range(0, len(c), 2):
    b = c[i:i+2]
    list1.append(b)
length = len(list1)
list2.append(".")
list2.append('00')
list2.append('00')
square = 0
div = 0
for i in range(1, int(list2[0])+1):
    if (i**2) > int(list2[0]):
        square = i-1
        div = i-1
        break
    elif (i**2) == int(list2[0]):
        square = i
        div = i
index = list2.index(".")

if int(list2[index-1]) == 0 or length == 1:
    print("The square root of {} is:".format(a), str(int(square))+"0"*int(count/2))
else:
    res = str(int(list2[0])-(divide*square))+list2[1]
    res = int(res)
    div = str(divide+square)
    while i==int(res):
        if 1.0 == res / (int(div + str(i)) * i):
            print("The square root of {} is:".format(a), str(int(square))+str(i))
            break
        else:
            res = res//(int(div + str(i))
