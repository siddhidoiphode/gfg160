import sys
n=input("").strip()
if n[0]=="-" :
    print("invalid input")
    sys.exit()

if n==n[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")







# Problem Statement – Goutam and  Tanul plays  by  telling numbers.  Goutam says a number to Tanul.  Tanul should first reverse the number and check if it is same as the original.  If yes,  Tanul should say “Palindrome”.  If not, he should say “Not a Palindrome”.  If the number is negative, print “Invalid Input”.  Help Tanul by writing a program.

# Sample Input 1 :

# 21212

# Sample Output 1 :

# Palindrome

# Sample Input 2 :

# 6186

# Sample Output 2 :

# Not a Palindrome