import sys

totalsem=int(input("Enter no of sem: "))
totalsubject=[]
print("subject per sem")
for i in range(totalsem):
    totalsubject.append(int(input()))
print(totalsubject)
subject=[]

for i in range(len(totalsubject)):
    temp=[]
    print("marks obtained all subject ",totalsubject[i])
    for j in range(int(totalsubject[i])):
        marks=int(input())
        if marks >100 or marks < 0:
            print("You have entered invalid mark.")
            sys.exit(0)
        temp.append(marks)
        

    subject.append(temp)


print(totalsem)
print(totalsubject)
print(subject)  

s=0
for i in subject:
    m=max(i)
    s+=1
    print(f"max mark in sem {s} : {m}")

# Problem Statement – Raj wants to know the maximum marks scored by him in each semester. The mark should be between 0 to 100 ,if goes beyond the range display “You have entered invalid mark.”

# Sample Input 1:

# Enter no of semester:
# 3

# Enter no of subjects in 1 semester:
# 3

# Enter no of subjects in 2 semester:
# 4

# Enter no of subjects in 3 semester:
# 2

# Marks obtained in semester 1:
# 50
# 60
# 70

# Marks obtained in semester 2:
# 90
# 98
# 76
# 67

# Marks obtained in semester 3:
# 89
# 76

 

# Sample Output 1:

# Maximum mark in 1 semester:70
# Maximum mark in 2 semester:98
# Maximum mark in 3 semester:89
# Sample Input 2:

# Enter no of semester:
# 3

# Enter no of subjects in 1 semester:
# 3

# Enter no of subjects in 2 semester:
# 4

# Enter no of subjects in 3 semester:
# 2

# Marks obtained in semester 1:
# 55
# 67
# 98

# Marks obtained in semester 2:
# 67
# -98

# Sample Output 2:

# You have entered invalid mark.

# Java	Python	C++
# Run
# no_of_sem =  int( input("Enter the no of sem"))
# list1=list()
# for i in range(no_of_sem):
#     print("Enter the no of subjects in sem",i+1)
#     list1.append(list(range(int(input()))))
# for i in range(no_of_sem):
#     print("Marks obtained in sem ",i+1)
#     for j in range(len(list1[i])):
#         list1[i][j]=int(input())
#         if not list1[i][j] in range(0,101):
#             print("You have Entered Invalid Marks")
#             exit()
# count = 1
# for i in list1:
#     print("Maximum marks in ", count," sem:",max(i))
#     count+=1
