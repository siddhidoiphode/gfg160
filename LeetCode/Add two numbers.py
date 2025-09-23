
l1 = [2, 4, 3, 9]
l2 = [5, 6, 4, 2, 2 ,5] 

result = []
carry=0

if len(l2) > len(l1) :
    l1,l2 =l2,l1

for i in range(len(l2)):
    total= carry+l1[i]+l2[i]
    result.append(total%10)
    carry=total//10

for i in range(len(l2),len(l1)):
    total= carry+l1[i]
    result.append(total%10)
    carry=total//10

if carry:
    result.append(carry)

print(result)


















# # Ensure l1 is the longer list
# if len(l2) > len(l1):
#     l1, l2 = l2, l1

# result = []
# carry = 0

# # Add digits while both lists have values
# for i in range(len(l2)):
#     total = l1[i] + l2[i] + carry
#     result.append(total % 10)
#     carry = total // 10

# # Add remaining digits from the longer list
# for i in range(len(l2), len(l1)):
#     total = l1[i] + carry
#     result.append(total % 10)
#     carry = total // 10

# # If carry is still left
# if carry:
#     result.append(carry)

