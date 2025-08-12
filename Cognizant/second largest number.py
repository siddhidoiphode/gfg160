
# arr = list(map(int , input((" ").split(" ")  )))
arr = list(map(int, input().strip("[]").split(",")))

second = float('-inf')
first = float('-inf')

for i in arr:
    # print(i)
    if i > first:
        second = first
        first = i
    
    elif i>second and i < first:
        second = i


print(second if second != float('-inf') else "no second largest number")









































