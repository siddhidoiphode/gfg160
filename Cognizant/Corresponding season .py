
# Problem Statement – Rhea Pandey’s teacher has asked her to prepare well for the lesson on seasons. When her teacher tells a month, she needs to say the season corresponding to that month. Write a program to solve the above task.

# Spring – March to May,
# Summer – June to August,
# Autumn – September to November and,
# Winter – December to February.
# Month should be in the range 1 to 12.  If not the output should be “Invalid month”.

# Sample Input 1:

# Enter the month:11
# Sample Output 1:

# Season:Autumn
# Sample Input 2:

# Enter the month:13
# Sample Output 2:

# Invalid month

import sys

dic = {
    1:"January",
    2:"February",
    3:"March" ,
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:'December'
}
month=int(input("Enter month: "))
ans=dic.get(month)
print(ans)
if month>12:
    print("Invalid Input")
    sys.exit(0)

if month<=5 and month>=3 :
    print("Spring")
elif month<=8 and month>=6 :
    print("Summer")
elif month<=11 and month>=9 :
    print("Autumn")
else:
    print("Winter")
