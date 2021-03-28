""" Design a Python script to sort numbers specified in a text file using lists."""
file_obj = open("numbers.txt", "b")
num_list = []
for num in file_obj:
    c = num.replace("\n", '')
    num_list.append(int(c))
num_list.sort()
print(num_list)
