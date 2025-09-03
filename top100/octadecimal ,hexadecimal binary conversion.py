# BINARY TO DECIMAL

print("-----------------------BINARY TO DECIMAL------------------------------------")

binary = '10010101101'
print("Binary number is ",binary)
decimal=int(binary,2)
print("deciaml number: ",decimal )
print("deciaml to Hexadecimal number: ",hex(decimal) )
print("deciaml to Octadecimal number: ",oct(decimal) )
print("deciaml to Binary number:", bin(decimal))


# In Python, when you use the bin() function, it automatically adds the prefix 0b in front of the number.
# 0b = tells Python “this is a binary literal”.
# Similarly:
# 0x = hexadecimal
# 0o = octal


print("-----------------------OCTAL TO DECIMAL--------------------------")
oct1='115'
print("deciaml number",int(oct1,8))

print()
print("--------------------HEXADECIMAL TO DECIMAL---------------")
h='4d'
print("decimal ",int(h,16))


print()
print("-------------------- DECIMAL TO BINARY ---------------")
num=88
print("Binary: ",bin(num))


print()
print("-------------------- DECIMAL TO OCTAL ---------------")
n1=77
print("octal : ",oct(n1))



print()
print("-------------------- DECIMAL TO HEXADECIMAL  ---------------")
n2=80
print("hexadecimal: ",hex(n2))

print()
print("-------------------- bINARY TO OCTAL ---------------")
b="11010100111"
print("binary->decimal->octal",oct(int(b,2)) )
 
print()
print("-------------------- OCTAL TO BINARY ---------------33333")
m='2255'
print("decimal",m)
print("octal ->  decimal -> binary",( bin(int(m,8)) ))

