import time

class Car:
    def __init__(self, brand):
        self.brand = brand
        print(f"{self.brand} car is created.")

    def __del__(self):
        print(f"{self.brand} car is destroyed.")

# Create object
car1 = Car("Honda")
car2=car1
# Delete the object directly

del car1
time.sleep(5)
print("car1 deleted. Program ends.")



