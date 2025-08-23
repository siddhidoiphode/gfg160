#     print("Season:Winter")

# else:
#     print("Invalid month")
# Question-7
# Problem Statement – To speed up his composition of generating unpredictable rhythms, Blue Bandit wants the list of prime numbers available in a range of numbers.Can you help him out?

# Write a java program to print all prime numbers in the interval [a,b] (a and b, both inclusive).

# Note

# Input 1 should be lesser than Input 2. Both the inputs should be positive. 
# Range must always be greater than zero.
# If any of the condition mentioned above fails, then display “Provide valid input”
# Use a minimum of one for loop and one while loop
# Sample Input 1:

# 2

# 15

# Sample Output 1:

# 2 3 5 7 11 13

# Sample Input 2:

# 8

# 5

# Sample Output 2:

# Provide valid input

import sys

start=int(input())
end=int(input())
n=start
if end<start or start <0 or end <0 :
    print("Provide valid input")
    sys.exit(0)

if start==0 or start==1:
    start=2

prime=[]
while start <= end:
    flag=0
    print("-",start)
    for i in range(2,(start//2)+1):
        if start % i ==0:
            flag+=1
    if flag==0:
        prime.append(start)

    start+=1

print(prime)

        
