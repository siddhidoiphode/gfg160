# Problem statement-: Elliot made a KeyLogger for his friend Romero, so that he can see the passwords of his friend. Keylogger is a software that can tell you the buttons pressed in the keyboard without the consent of the user, and hence unethical. Elliot made it to hack Romero’s passwords. The one problem is, Romero writes the passwords in lowercase characters only, and the keylogger only takes the values of the keys. Like, for a it takes 1, for b 2, and for z 26. For a given number Elliot produces all combinations of passwords in a dictionary and starts a dictionary based password attack. For a given number, print all the possible passwords in a lexicographic order.

# Input Format:

# One line, denoting the value given by the keylogger
# Output Format:

# All possible combinations of keyloggers in new lines are lexicographically ordered.
# Constraints:

# 2<=Number of digit in input<=1000
# Sample Input:

# 1234

# Sample Output:

# abcd

# awd

# lcd

# Explanation:

# For 12, you can take 1,2 that is ab, or you can take l.\\

digits="1234"
alpha = { str(i): chr(96+i) for i in range(1,27) }
print(alpha)
n=len(digits)
result = []

# alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# nums =  [ 1 , 2 , 3 , 4 , 5, 6 , 7 , 8 , 9 , 10 , 11 ,12, 13, 14 ,15, 16 ,17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

# x='1234'
# y=list(x)
# print(y)
# row=''
# for i in y:
#     if int(i) in nums:
#         ind=nums.index(int(i))
#         row+=alpha[ind]

# print(row)

# for i in range(len(x)):
#     ele = x[i:i+2]    
#     if ele in x:
#         print(row[])
#     print(ele)

