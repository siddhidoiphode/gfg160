
n=int(input("enter year : "))

if (n%4 == 0):
    # print("leap")
    if(n%100 == 0):
        if(n%400==0):
            print("leap 1")
        else:
            print("not leap 2")
    else:
       print("not leap 4")
else:
    print("not leap 3")



# if(year%4==0):
#   if(year%100==0):
#     if(year%400==0):
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year")