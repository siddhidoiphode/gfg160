# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")

# a,b=map(int,input("").split())
# # b=int(input())
# # c = a+b
# print(a+b)

# text = input()
# s=[]
# s=text.split()
# print(s)
# for i in range(len(s)-1,-1,-1):
#     print(s[i] ,end=" ")



class Hotel :
    def __init__(self , name , fare ):
        self.name = name
        self.fare = fare

    def __gt__(self , other):
        return self.fare > other.fare
    

h1=Hotel('A',100000)
h2=Hotel('B',200000)

print(h1>h2)



# print(h1.fare > h2.fare)
# print(dir(str))



