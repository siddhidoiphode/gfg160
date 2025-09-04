
n=123003204
new=''
easy=""
print(str(n).replace("0",'1'))

new = "".join("1" if x == "0" else x for x in str(n))

# e = "".join(str(map(str, i for i in str(n))))
print("Loop use karun :",new)

