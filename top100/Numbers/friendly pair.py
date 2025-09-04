a=int(input("Enter number: "))
b=int(input("Enter number: "))

a_divisors=[i for i in range(1,(a//2)+1) if a%i==0]
b_divisors=[i for i in range(1,(b//2)+1) if b%i==0]

# if ( (a+sum(a_divisors))/a == (b+sum(b_divisors))/b ):
#     print("Friendly pair",a,b)

print( "Friendly pair"  if (a+sum(a_divisors))/a == (b+sum(b_divisors))/b else " Not Friendly pair" )




# Two numbers A and B are called a friendly pair if

# Sum of divisors of A
# 𝐴
# =
# Sum of divisors of B
# 𝐵
# A
# Sum of divisors of A
# 	​

# =
# B
# Sum of divisors of B
# 	​
# # 