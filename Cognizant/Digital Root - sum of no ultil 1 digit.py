
# n=int(input("Enter a number: "))
# while len(str(n))!=1:
#     s=0
#     for i in str(n):
#         s+=int(i)
#     n=s
#     print(n)

# print("final: ",n)

n=12345
while(len(str(n))) != 1:
    s=0
    for i in str(n):
        s+=int(i)
    print(n)
    n=s
print(n)