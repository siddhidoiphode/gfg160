
def decorator1(func):
    def wrapper(*args):
        print('start')
        func(*args)
        print('end')
    return wrapper

@decorator1
def add(*args):   
    print(sum(*args))


add([1,3,2,3,2,34])
# print(add(10,3))

