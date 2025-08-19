import os

file = open("P:/Python/Advenced Python SimpliLearn/sample.txt",'r')


###### READ #######
print(file.read())

# abc
# def
# \
# this is a sample file
# for file handling
# ok
# P:\Python\Advenced Python SimpliLearn\sample.txt
# sample.txt


print(file.readlines())
# ['abc\n', 'def\n', '\\\n', 'this is a sample file\n', 'for file handling \n', 'ok\n', 'P:\\Python\\Advenced Python SimpliLearn\\sample.txt\n', 'sample.txt']

print(file.read(5))
# abc
# d

print(file.readline(4)) 
# abc

print(file.readlines(8)) 
# ['abc\n', 'def\n', 'this is a sample file\n']


print(file.readlines(4)) 
# ['abc\n', 'def\n']

print(file.readlines(7)) 
# ['abc\n', 'def\n']

# file.close()

file1 = open("P:/Python/Advenced Python SimpliLearn/sample.txt", 'w')
file1.write("sunday monday")  # Write content and it returns the number of characters (13)
file1.close()

# Now, open the file in read mode and print the content
file1 = open("P:/Python/Advenced Python SimpliLearn/sample.txt", 'r')
content = file1.read()  # Read the content from the file
print(content)  # Output: sunday monday
file1.close()


file1 = open("P:/Python/Advenced Python SimpliLearn/sample2.txt", 'x')
print(file1.write("new file2"))
file1.close()
file1 = open("P:/Python/Advenced Python SimpliLearn/sample1.txt", 'r')
x= file1.read()
print(x)
file1.close()

# sunday monday
# 9
# new file


# ----------------------------  DELETION  ---------------------------------------------

import os
os.remove("P:/Python/Advenced Python SimpliLearn/sample1.txt")

if os.path.os.exists("P:/Python/Advenced Python SimpliLearn/sample2.txt") :
    os.remove("P:/Python/Advenced Python SimpliLearn/sample2.txt")
else:
    print("not exists")

    
