
n = 12345
rev = 0
orig = n

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10  

print(rev==orig)



# n = 123456
# rev=0
# # print(str(n))
# l=0

# mul= 10 **(len(str(n))-1)
# print(mul)
# while n%10 != 0:
#     v=n%10
#     rev+= mul*v
#     print("-",rev)
#     mul/=10
#     n=n//10

# print(rev)
