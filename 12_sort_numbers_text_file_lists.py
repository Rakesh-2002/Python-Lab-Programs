""" Design a Python script to sort numbers specified in a text file using lists."""
file_obj = open("numbers.txt", "r")
num_list = []
for num in file_obj:
    a = num.replace("\n", '')
    num_list.append(int(a))
num_list.sort()
print(num_list)
