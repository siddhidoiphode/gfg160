
def check_age(age):
    if age < 0 :
        raise Exception ("age must be > 0")
    if age < 18:
        # Raise a custom exception if the condition is not met
        raise Exception("Age must be at least 18")
    
    else:
        print("Access granted.")

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
    
except Exception as e:
    print("Error:", e)

