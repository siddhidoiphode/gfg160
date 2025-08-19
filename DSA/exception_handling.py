try:
    a=1
    b=0
    c=a/b
except ZeroDivisionError:
    print("cannot divide by zero")
except TypeError :
    print("unsupported operation ")


try:
    d=1
    if d < 2:
        raise Exception("Cannot have values less than 2.")
except Exception as e:
    print(e)



def chaeck_age(age):
    if age < 18 :
        raise ValueError("age should be greater than 18") 
    else:
        print("go ahead")

try:
    chaeck_age(1)
except :
    print("error")



try:
    risk = 10/1
except Exception as e:
    print(e)
else:
    print("valid operation")
finally :
    print(" execution successful !")

# PS P:\Python\Advenced Python SimpliLearn> & "C:/Users/Siddhi Doiphode/AppData/Local/Programs/Python/Python312/python.exe" "p:/Python/Advenced Python SimpliLearn/exception_handling.py"
# cannot divide by zero
# Cannot have values less than 2.
# error
# division by zero
#  execution successful !
