
itemlist=[]
n=int(input("Enter number of items: "))
for i in range(n):
    # ele=input().split(",")
    itemlist.append(input().split(","))


print(itemlist)
discount=[]
item=[]

for items in itemlist:
    dis=( int(items[2]) * int(items[1]) )/100 
    discount.append(dis)
    item.append(items[0])

print(itemlist)
print(discount)
print(item)

m=min(discount)

for i in range(len(discount)):
    if discount[i]==m:
        print(item[i])



# Question-12
# Problem Statement – Mayuri buys “N” no of products from a shop. The shop offers a different percentage of discount on each item. She wants to know the item that has the minimum discount offer, so that she can avoid buying that and save money.
# [Input Format: The first input refers to the no of items; the second input is the item name, price and discount percentage separated by comma(,)]
# Assume the minimum discount offer is in the form of Integer.

# Note: There can be more than one product with a minimum discount.

# Sample Input 1:

# 4

# mobile,10000,20

# shoe,5000,10

# watch,6000,15

# laptop,35000,5

# Sample Output 1:

# shoe

# Explanation: The discount on the mobile is 2000, the discount on the shoe is 500, the discount on the watch is 900 and the discount on the laptop is 1750. So the discount on the shoe is the minimum.

# Sample Input 2:

# 4

# Mobile,5000,10

# shoe,5000,10

# WATCH,5000,10

# Laptop,5000,10

# Sample Output 2:

# Mobile 

# shoe 

# WATCH 

# Laptop

# Java	Python	C++
# Run
# items = int(input())
# itemList=[]
# for i in range(items):
#     itemList.append(input().split(","))
# list2=[]
# for i in itemList:
#     i.append((int(i[1])*int(i[2]))//100)
#     list2.append(i[3])
# result=[]  
# minimum = min(list2)
# for i in itemList:
#     if i[3] == minimum:
#         result.append(i[0])
# for i in result:
#     print(i)