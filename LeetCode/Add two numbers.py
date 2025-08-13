# l1=[2, 4, 3, 9]
# l2=[5, 6, 4, 2 ,2]

# max_list=max(l1,l2)
# if len(l1) > len(l2):
#     max_list=l1
# elif len(l2) > len(l1):
#     max_list=l2
# elif len(l1) == len(l2):
#     max_list=l1



# min_l=min(len(l1), len(l2))
# print("maxlist",max_list ,"min len", min_l)
# max_l=len(max_list)
# d=0
# A=[]

# for i in range(min_l):
        
#         if i==min_l - 1 :
#             a=l1[i] + l2[i]+d
#             A.append(a) 
#         else:
#             a=l1[i] + l2[i]+d
#             m=a%10
#             d=a//10
#             A.append(m)

# for j in range(min_l, max_l):
        
#         if j==max_l - 1 :
#             a=max_list[j]+d
#             A.append(a)  
#         else:
#             a=max_list[j]+d
#             m=a%10
#             d=a//10
#             A.append(m)


# print(l1)
# print(l2)
# print(A)



l1 = [2, 4, 3, 9]
l2 = [5, 6, 4, 2, 2 ,5]

# Ensure l1 is the longer list
if len(l2) > len(l1):
    l1, l2 = l2, l1

result = []
carry = 0

# Add digits while both lists have values
for i in range(len(l2)):
    total = l1[i] + l2[i] + carry
    result.append(total % 10)
    carry = total // 10

# Add remaining digits from the longer list
for i in range(len(l2), len(l1)):
    total = l1[i] + carry
    result.append(total % 10)
    carry = total // 10

# If carry is still left
if carry:
    result.append(carry)

